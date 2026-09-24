#!/usr/bin/env bash
# Log in to de-crypt.org (DECODE, the DECRYPT project's cipher database) and save a record page plus its
# attached files to a directory. Credentials come from the environment (DECODE_USER, DECODE_PASS); never
# pass them on the command line or print them.
#
#   tools/decode_fetch.sh RECORD_ID OUT_DIR
#
# Flow (worked out 20 Sept 2026, PHPMaker-generated "decryptweb23" app, no client-side password encryption
# despite the ENCRYPTED_PASSWORD site flag -- that flag only controls server-side hashing):
#   1. GET /decrypt-web/login to obtain a fresh csrf_name/csrf_value pair and a PHPSESSID cookie.
#   2. POST username, password and that csrf pair to the same URL, keeping the cookie jar.
#   3. A login failure re-renders the same login form (HTTP 200, IS_LOGGEDIN:false in the embedded JSON) --
#      there is no redirect or distinct status code to key off, so success is judged by IS_LOGGEDIN:true.
#   4. On success, GET /decrypt-web/RecordsView/RECORD_ID with the same cookie jar for the record page, then
#      the record's Documents/Images sub-pages or file links for attachments.
set -euo pipefail

RECORD_ID="${1:?usage: decode_fetch.sh RECORD_ID OUT_DIR}"
OUT_DIR="${2:?usage: decode_fetch.sh RECORD_ID OUT_DIR}"
BASE="https://de-crypt.org/decrypt-web"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"

if [ -z "${DECODE_USER:-}" ] || [ -z "${DECODE_PASS:-}" ]; then
  echo "DECODE_USER/DECODE_PASS: unset" >&2
  exit 2
fi

mkdir -p "$OUT_DIR"
COOKIE_JAR="$(mktemp)"
LOGIN_PAGE="$(mktemp)"
trap 'rm -f "$COOKIE_JAR" "$LOGIN_PAGE"' EXIT

curl -sS -A "$UA" -c "$COOKIE_JAR" -o "$LOGIN_PAGE" "$BASE/login"

CSRF_NAME=$(grep -o 'name="csrf_name" value="[^"]*"' "$LOGIN_PAGE" | sed 's/.*value="//;s/"$//')
CSRF_VALUE=$(grep -o 'name="csrf_value" value="[^"]*"' "$LOGIN_PAGE" | sed 's/.*value="//;s/"$//')
if [ -z "$CSRF_NAME" ] || [ -z "$CSRF_VALUE" ]; then
  echo "could not find csrf_name/csrf_value on the login page; site markup may have changed" >&2
  exit 3
fi

# Post every field the form itself would post (24 Sept 2026): the hidden inputs besides the CSRF pair (e.g. "login")
# and the submit button ("btn-submit"), plus Origin/Referer, so the server treats it as the form's own submission.
# Earlier attempts posted only the four named fields; the page came back re-rendered with IS_LOGGEDIN:false and no
# "Incorrect user name or password" message, which is what an unrecognised submission looks like, not a bad password.
EXTRA_ARGS=()
while IFS= read -r tag; do
  # `|| true`: a <button> without a value attribute made grep exit 1 inside $(...), and set -e then killed the script
  # silently before any POST (24 Sept 2026 04:39 UTC, the first run of the repaired form).
  n=$(printf '%s' "$tag" | { grep -o 'name="[^"]*"' || true; } | head -1 | sed 's/name="//;s/"$//')
  v=$(printf '%s' "$tag" | { grep -o 'value="[^"]*"' || true; } | head -1 | sed 's/value="//;s/"$//')
  case "$n" in csrf_name|csrf_value|username|password|"") continue;; esac
  EXTRA_ARGS+=(--data-urlencode "$n=$v")
done < <(grep -o '<input[^>]*type="hidden"[^>]*>\|<button[^>]*type="submit"[^>]*>' "$LOGIN_PAGE")
LOGIN_RESULT="$(mktemp)"
curl -sS -A "$UA" -b "$COOKIE_JAR" -c "$COOKIE_JAR" -o "$LOGIN_RESULT" \
  -H "Origin: https://de-crypt.org" -H "Referer: $BASE/login" -H "Accept: text/html,application/xhtml+xml" \
  --data-urlencode "csrf_name=$CSRF_NAME" \
  --data-urlencode "csrf_value=$CSRF_VALUE" \
  --data-urlencode "username=$DECODE_USER" \
  --data-urlencode "password=$DECODE_PASS" \
  "${EXTRA_ARGS[@]}" \
  "$BASE/login"

if ! grep -q '"IS_LOGGEDIN":true' "$LOGIN_RESULT"; then
  if grep -qi 'incorrect user name or password' "$LOGIN_RESULT"; then
    echo "login rejected: the server showed 'Incorrect user name or password' (the values in DECODE_USER/DECODE_PASS are wrong for this site; do not retry blindly, repeated failures can lock the account)" >&2
  else
    echo "login not accepted: page re-rendered with IS_LOGGEDIN:false and NO 'incorrect' message (the submission itself was not recognised; extra fields posted: ${#EXTRA_ARGS[@]}/2). Check the form markup before retrying." >&2
  fi
  rm -f "$LOGIN_RESULT"
  exit 4
fi
rm -f "$LOGIN_RESULT"

curl -sS -A "$UA" -b "$COOKIE_JAR" -o "$OUT_DIR/record_${RECORD_ID}.html" "$BASE/RecordsView/$RECORD_ID"

# Attached files are linked from the record page as /decrypt-web/uploads/... or a file-download action;
# pull every such href/src found on the page. Adjust the pattern if a given record's markup differs.
grep -o '"[^"]*\(uploads\|api/file\)[^"]*"' "$OUT_DIR/record_${RECORD_ID}.html" \
  | tr -d '"' | sort -u | while read -r href; do
    case "$href" in
      http*) url="$href" ;;
      /*) url="https://de-crypt.org$href" ;;
      *) url="$BASE/$href" ;;
    esac
    fname=$(basename "${url%%\?*}")
    [ -n "$fname" ] || continue
    curl -sS -A "$UA" -b "$COOKIE_JAR" -o "$OUT_DIR/$fname" "$url" || echo "failed to fetch $url" >&2
  done

echo "saved record $RECORD_ID to $OUT_DIR"
