

#install net.security from github devel branch
#devtools::install_github(repo = "r-net-tools/net.security", ref = "devel")
library(net.security)

#extract datagrame from net.security pacage
cves <- GetDataFrame("cves")
cpes <- GetDataFrame("cpes")

