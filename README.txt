The Mall Makeover - prototype (light version)

Files
  index.html            the game (all code inside)
  assets/               all pictures, as WebP (smaller files, same look)
  manifest.webmanifest  + icons/   home-screen name and icon (full-screen launch on Android)
  serve.py              local test server (python serve.py -> http://127.0.0.1:8765/)
  optimize_assets.py    converts any new PNG you add to assets/ into WebP (see inside)

Run it
  python serve.py       then open http://127.0.0.1:8765/

On a phone (full screen)
  iPhone (Safari): a web page cannot hide Safari's bars by itself. Open the link, tap Share -> "Add to Home
    Screen", then start the game from the new "Mall Makeover" icon: it opens full screen, without bars.
  Android (Chrome): the first tap on the start screen switches to full screen. For an app-like icon use the
    menu -> "Add to Home screen" / "Install app" (landscape, full screen).
  Turn the phone sideways: the game is landscape.

Publishing
  Upload the whole folder to any static hosting (Netlify Drop, GitHub Pages, Cloudflare Pages ...).
  index.html must stay in the root of the folder, next to the assets folder.

Notes
  - Every picture the game uses is in assets/.
  - brush-dust.webp is the broom that sweeps the start screen away; reward-coin.webp and reward-gem.webp are in the folder but the game does not use them yet.
  - To change a picture, replace the file in assets/ with the same name (the Splashscreen is read straight
    from assets/Splashscreen.webp). If you have a PNG, put it in assets/ and run:  python optimize_assets.py
  - The result screens (Stage Complete, Makeover Complete, Let's Go Again) and the broom/coins corners
    are embedded inside index.html, so replacing files in assets/ does not change them.
