# Shurike

Shuriken is a suite that manages a set of system audit tools. This proyect is the result of the final project of master in Cybersecurity and Management studied in [UPC School](https://www.talent.upc.edu).

The project has three main branches: the first one is Python Crawler based on [Scrapy Crawler](https://scrapy.org/), the second one is R Shiny WebApp that use [net.security package](https://github.com/r-net-tools/net.security) and the third is a tool to manage an instance of [OpenVas](http://www.openvas.org/)

Given these three tools, it allows you to extract information about system vulnerabilities and then you can view them in an organized way. It allows two ways of extracting data, using the crawler or openvas. Para visualizarlos integra una dashboard que relaciona los resultados.

The Crawler have three modules that run consecutively to extract information at the web level as protocol level and open ports as well as physical location:
* [Scrapy Crawler](https://scrapy.org/)
* [Nikto](https://cirt.net/Nikto2)
* [Nmap](https://nmap.org/)
* [GeoIP](https://pypi.python.org/pypi/GeoIP/)
* [Wig](https://github.com/jekyc/wig)


## Install


It has been tested on Kali Linux systems

For installation it is necessary:
* [Python 2.7.12](https://www.python.org/downloads/)
* [R 3.3.2](https://www.r-project.org/)


It is also necessary to have installed in the sistem: Scrapy, Nikto, Nmap, GeoIP, Wig, OpenVas.

At the moment a setup file has not been generated so it is necessary to manually install the following package of Python and R.

Python packages:
* colored
* cvs
* nmap
* scapy
* logging
* GeoIP
* scrapy


R packages:
* shiny
* shinydashboard
* ggplot2
* leaflet
* XML
* stringr
* dplyr
* tidyr
* rworldmap
* net.security

