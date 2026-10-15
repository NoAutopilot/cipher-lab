"""C1161-SSPLIT addendum (15 Oct 2026): place sign POS of a line by ink segments, not even spacing.
Band = rows around the strip's ink peak (the line's own writing); columns of the band split at blank runs into segments;
segment k of n maps to sign index by rank (k+0.5)/n ~ (pos-0.5)/nsigns. Returns the x centre and mean segment pitch."""
import numpy as np
def locate(S, nsigns, pos, ink=90):
    A = np.array(S)
    dead = (A < 40).mean(0) > 0.6            # black paste borders / margins
    I = (A < ink) & ~dead[None, :]
    prof = I.sum(1).astype(float)
    k = np.convolve(prof, np.ones(41) / 41, 'same'); c = int(np.argmax(k[30:-30]) + 30) if len(k) > 60 else len(k) // 2
    band = I[max(0, c - 35):c + 35]
    col = band.sum(0) >= 2
    segs, x = [], 0
    W = len(col)
    while x < W:
        if col[x]:
            s = x
            gap = 0
            while x < W and gap < 6:
                gap = 0 if col[x] else gap + 1; x += 1
            segs.append((s, x - gap))
        else:
            x += 1
    segs = [t for t in segs if t[1] - t[0] >= 8]
    if not segs:
        return None, None, c
    n = len(segs); want = (pos - 0.5) / nsigns
    j = min(range(n), key=lambda i: abs((i + 0.5) / n - want))
    pitch = (segs[-1][1] - segs[0][0]) / max(1, nsigns)
    return (segs[j][0] + segs[j][1]) // 2, pitch, c
