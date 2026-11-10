# playcord-web

The public pages behind PlayCord's gift list links. They hold no code from the app and no secrets: each page reads
from PlayCord's server by the secret after the `#` in its link, which never reaches this host.

- `wishlist.html`: a member's gift list, for Christmas or any occasion. Its preview card for Messages and the like is
  `og-gift-list.png`.
- `stop.html`: the stop link in PlayCord's emails to people getting a record from a gift list (`?what=news` for its
  news). Nothing happens until its button is pressed.
- `news.html`: "Yes, send me them" from the last of those emails. Nothing happens until its button is pressed.
- `playcord-logo.png`, `apple-touch-icon.png`, `favicon.svg`, `favicon-32.png`: PlayCord's record, for emails, home
  screens and browser tabs.
- `index.html`: PlayCord's home page at playcord.app (preview card `og-playcord.png`). `invite.html`: the page a friend
  invite opens (preview card `og-invite.png`).
- `about.html`, `terms.html`, `privacy.html`, `support.html`, `complaints.html`: the legal and help pages. These are
  written by the PlayCord repository's `scripts/web-pages.ts` (`npx tsx scripts/web-pages.ts ../playcord-web`), so
  change them there, not here.
- `csp.py`: adds each page's Content-Security-Policy. Run `python3 csp.py .` after changing any page's script.
- `CNAME` (the playcord.app domain) and `robots.txt` (only link-preview bots may read the pages).
