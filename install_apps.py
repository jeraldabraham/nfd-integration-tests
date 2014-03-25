#!/usr/bin/python
import os
from os.path import expanduser

# Setup Preparation Folders
print "\n[01/09] SETTING UP PREPARATION FOLDERS"
print "**************************************"
home = expanduser("~")
os.chdir(home)
os.system("rm -rf nfd_prepare")
os.system("mkdir nfd_prepare")

# Install Dependencies & Necessary Tools
print "\n[02/09] INSTALLING DEPENDENCIES"
print "*******************************"
os.system("sudo apt-get -qq install software-properties-common python-software-properties")
os.system("sudo add-apt-repository -y ppa:named-data/ppa")
os.system("sudo apt-get -qq update")
os.system("sudo apt-get -qq install ndnx-dev libboost1.48-all-dev libcrypto++-dev pkg-config libsqlite3-dev")

# Fetch Apps From Their Gerrit Repositories
print "\n[03/09] FETCHING LATEST APP SOURCE CODES FROM GERRIT"
print "****************************************************"
os.chdir("nfd_prepare")
os.system("rm -rf ndn-cpp-dev ndnd-tlv NFD ndn-traffic-generator ndn-tlv-ping")
os.system("git clone http://gerrit.named-data.net/ndn-cpp-dev")
os.system("git clone http://gerrit.named-data.net/ndnd-tlv")
os.system("git clone http://gerrit.named-data.net/NFD")
os.system("git clone http://gerrit.named-data.net/NFD/ndn-traffic-generator")
os.system("git clone http://gerrit.named-data.net/ndn-tlv-ping")

# Install ndn-cpp-dev
print "\n[04/09] INSTALLING ndn-cpp-dev"
print "******************************"
os.chdir("ndn-cpp-dev")
os.system("./waf distclean")
os.system("./waf configure")
os.system("./waf -j1")
os.system("sudo ./waf install")
os.chdir("..")

# Install ndnd-tlv
print "\n[05/09] INSTALLING ndnd-tlv"
print "***************************"
os.chdir("ndnd-tlv")
os.system("./waf distclean")
os.system("./waf configure")
os.system("./waf -j1")
os.system("sudo ./waf install")
os.chdir("..")

# Configure Security Environment With ndn-cpp-security-tools
print "\n[06/09] CONFIGURING SECURITY ENVIRONMENT WITH ndn-cpp-decurity-tools"
print "********************************************************************"
os.system("mkdir /tmp/nfd_integration_tests/")
os.system("ndnsec-keygen -n '/tmp/nfd_integration_tests/' | ndnsec-install-cert -")

# Install NFD
print "\n[07/09] INSTALLING NFD"
print "**********************"
os.chdir("NFD")
os.system("./waf distclean")
os.system("./waf configure")
os.system("./waf -j1")
os.system("sudo ./waf install")
os.system("sudo mkdir /usr/local/etc/nfd/")
os.system("sudo cp /usr/local/etc/ndn/nfd.conf.sample /usr/local/etc/nfd/nfd.conf")
os.system("sudo cp /usr/local/etc/ndn/nfd.conf.sample /usr/local/etc/ndn/nfd.conf")
os.system("sudo mkdir /usr/local/etc/nfd/keys/")
os.system("sudo mkdir /usr/local/etc/ndn/keys/")
os.system("ndnsec-cert-dump -i `ndnsec-get-default` > ~/default.ndncert")
os.system("sudo cp ~/default.ndncert /usr/local/etc/nfd/keys")
os.system("sudo mv ~/default.ndncert /usr/local/etc/ndn/keys")
os.chdir("..")

# Install ndn-traffic-generator
print "\n[08/09] INSTALLING ndn-traffic-generator"
print "****************************************"
os.chdir("ndn-traffic-generator")
os.system("./waf distclean")
os.system("./waf configure")
os.system("./waf -j1")
os.system("sudo ./waf install")
os.chdir("..")

# Install ndn-tlv-ping
print "\n[09/09] INSTALLING ndn-tlv-ping"
print "*******************************"
os.chdir("ndn-tlv-ping")
os.system("./waf distclean")
os.system("./waf configure")
os.system("./waf -j1")
os.system("sudo ./waf install")
os.chdir("..")
