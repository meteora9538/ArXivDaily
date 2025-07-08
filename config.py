# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Authentication for user filing issue (must have read/write access to repository to add issue to)
USERNAME = 'meteora9538'

# The repository to add this issue to
REPO_OWNER = 'meteora9538'
REPO_NAME = 'ArXivDaily_AngularMomentum'

# Set new submission url of subject
NEW_SUB_URL = 'https://arxiv.org/list/astro-ph/new'

# Keywords to search
KEYWORD_LIST = ["star formation", "star-forming", "angular momentum", "spin", "disk galaxy", "fast rotator", "IMF", "environment", "brightest cluster galaxies", "H alpha emitter"]
# Keywords to exclude
KEYWORD_EX_LIST = ["gravitational wave"]
# Note that the 'Keywords' above are actually searched in the abstract instead of the real keyword section. 
