# The 18 November 2026 front page (Python 3.13, standard library only).
# The image is built into this repository at assets/entry.png: a generated
# editorial illustration of the day's top story (the APEC summit gathering
# in Shenzhen) under a masthead naming the date, with five reported stories
# set as crisp text. Copying a fixed file is byte-for-byte deterministic,
# so two runs always write the same bytes.
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, 'assets', 'entry.png'),
                os.path.join(OUT, 'entry.png'))
