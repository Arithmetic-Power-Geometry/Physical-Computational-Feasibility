# Evidence register

Statuses: **VERIFIED** (independently calculated/checked and reproducible), **SOURCE-REPORTED** (in current paper), **TO AUDIT**, **NOT ESTABLISHED**.

| ID | Claim | Status at P00 | Required independent evidence |
|---|---|---|---|
| E001 | 5-variable sets A and B as printed | SOURCE-REPORTED | literal truth-set extraction and independent graph builder |
| E002 | edge count 21, 12 isolated vertices each | SOURCE-REPORTED | exact edge lists and histogram |
| E003 | active components (16,4) vs (11,9) | SOURCE-REPORTED | exact traversal and vertex partitions |
| E004 | diameters (6,2) vs (4,4) | SOURCE-REPORTED | exact BFS distance matrix |
| E005 | identical integer characteristic polynomial | SOURCE-REPORTED | independent integer charpoly and compact Gram proof |
| E006 | bs, D, C0, C1, real/F2 degrees, directional controls | TO AUDIT | independent exact algorithms |
| E007 | n=5,k=4 canonical count 625, strong separation 0 | TO AUDIT | formal group, enumerator, independent checker |
| E008 | n=5,k=5 canonical count 2674, strong separation 1 | TO AUDIT | exact 201376-case enumeration, no unsafe pruning |
| E009 | same summary for all N>=5 under parity product | TO AUDIT | formal proof with r=0/r>0 cases |
| E010 | smallest possible dimension n=5 | NOT ESTABLISHED | full smaller-dimensional computation/proof |
| E011 | no prior known equivalent construction | NOT ESTABLISHED | extensive switching and restricted cut-graph literature audit |
| E012 | corresponding author metadata | USER-REQUESTED | author-confirmed revised front matter |

No experiment or theorem is claimed complete at P00. The original article's statements remain source-reported until verification files are added in subsequent commits.
