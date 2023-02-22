title="Action"
athelete=echo
# gen track
python3 scripts/gpx_sync.py

# gen github type record
python3 scripts/gen_svg.py --from-db --title "$title" --type github --athlete $athelete --special-distance 10 --special-distance2 20 --special-color yellow --special-color2 red --output assets/github.svg --use-localtime --min-distance 0.5

# gen grid
title="All Tracks"
python3 scripts/gen_svg.py --from-db --title "$title" --type grid --athlete $athelete  --output assets/grid.svg --min-distance 1.0 --special-color yellow --special-color2 red --special-distance 20 --special-distance2 40 --use-localtime

# gen static page
yarn build

# sync data to server
rsync -a -e "ssh -p 22" ./public  root@linxin.info:/root
