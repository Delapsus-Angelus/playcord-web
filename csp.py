# Adds a Content-Security-Policy to each PlayCord web page: its own inline scripts by hash, nothing else run or loaded
# beyond what the page needs. Run again after any script changes (it replaces the old one).
import base64, hashlib, re, sys, pathlib
SUPA = 'https://fyswlovbnndgbipmpquv.supabase.co'
COVERS = 'https://coverartarchive.org https://archive.org https://*.archive.org'
EXTRA = {'wishlist.html': {'connect-src': SUPA, 'img-src': COVERS}, 'news.html': {'connect-src': SUPA}, 'stop.html': {'connect-src': SUPA}}
root = pathlib.Path(sys.argv[1])
for f in sorted(root.glob('*.html')):
    s = f.read_text()
    s = re.sub(r'<meta http-equiv="Content-Security-Policy"[^>]*>\n', '', s)
    hashes = ["'sha256-%s'" % base64.b64encode(hashlib.sha256(m.encode()).digest()).decode() for m in re.findall(r'<script>(.*?)</script>', s, re.S)]
    extra = EXTRA.get(f.name, {})
    parts = ["default-src 'none'", "script-src " + (' '.join(hashes) or "'none'"), "style-src 'unsafe-inline'",
             "img-src 'self' data:" + (' ' + extra['img-src'] if 'img-src' in extra else ''),
             "connect-src " + extra.get('connect-src', "'none'"), "base-uri 'none'", "form-action 'none'"]
    meta = '<meta http-equiv="Content-Security-Policy" content="%s">\n' % '; '.join(parts)
    anchor = '<meta name="referrer" content="no-referrer">\n'
    assert anchor in s, f.name
    s = s.replace(anchor, anchor + meta, 1)
    f.write_text(s)
    print(f.name, len(hashes), 'scripts')
