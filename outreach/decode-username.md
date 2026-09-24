to: de-crypt.org/decrypt-web/login (your browser, then the environment variables; no email)
subject: DECODE login: confirm the User Name by hand, then set DECODE_USER to it
checked: 24 Sept 2026, orchestrator. Two single attempts with the values you reset (23 Sept 21:56 and 24 Sept 00:47 UTC) were rejected with the same non-secret signal, IS_LOGGEDIN:false. The login form asks for a "User Name"; the variable holds an email address. No password has been printed anywhere.
status: done 24 Sept 2026 (login works; user name confirmed)

# Two minutes, then tick the box

## Text
1. Open https://de-crypt.org/decrypt-web/login in your browser and log in by hand. If that fails too, use the site's password reset; the account may not be what you think it is.
2. Note the exact User Name the site accepts (DECODE usernames are chosen at registration and are often not the email).
3. In the ytbiz environment settings, set DECODE_USER to that user name and DECODE_PASS to the password that worked. Save.
4. Tick this box. The next orchestrator check-in makes one login attempt with the new pair and, if it works, pulls record 8725 and the full catalogue (ASSIGNMENTS row 7).
