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
