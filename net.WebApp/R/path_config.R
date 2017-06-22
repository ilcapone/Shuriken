# path for tests
#D:/CYBERSECURITY MANAGMENT (Master)/CyS/TFM/ShurikenRepository/

# Path app
netSecurity <- getwd()
netSecurity_path <- paste(netSecurity, "/net.WebApp", sep = "")

# Path of directoris
#data_path <- paste(netSecurity_path, "/data", sep="")
data_path <- paste(netSecurity, "/data/netSecurity_data", sep="")
R_path <- paste(netSecurity_path, "/R", sep="")

# Path of R scripts
confing_enviromet_path <- paste(R_path, "/config_enviroment.R", sep = "")
extractInfo_path <- paste(R_path, "/extractInfo.R", sep = "")
load_Dataframes_path <- paste(R_path, "/load_Dataframes.R", sep = "")

# Path of data files
crawler_links_path <- paste(data_path, "/crawler_links.csv", sep = "")
geoIP_crawlerIP_path <- paste(data_path, "/geoIP_crawlerIP.csv", sep = "")
nikto_crawler_links_path <- paste(data_path, "/nikto_crawler_links.csv", sep = "")
nmap_crawler_path <- paste(data_path, "/nmap_crawler.csv", sep = "")
openvas_path <- paste(data_path, "/openvas_data.xml", sep = "")

# Path of openvas data files
openvas_filesData_path <- paste(data_path, "/openvas", sep = "")