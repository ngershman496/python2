import pygeoip
import sys
import re


def get_info(ip):
    get_country(ip)
    get_city(ip)
    get_postalcode(ip)
    get_isp(ip)
    get_org(ip)


def get_rec(ip):
    gi = pygeoip.GeoIP('GeoIPCity.dat')
    return str(gi.record_by_addr(ip))


def get_city(ip):
    rec = get_rec(ip)
    rec = re.findall('\'city\': \'.*\'latitude\'', rec)
    rec = str(rec)
    rec = rec[11:-15]
    print('City: ' + rec)


def get_country(ip):
    rec = get_rec(ip)
    rec = re.findall('\'country_name.*\'cont', rec)
    rec = str(rec)
    rec = rec[19:-10]
    print('Country: ' + rec)


def get_postalcode(ip):
    rec = get_rec(ip)
    rec = str(re.findall('\'postal_code.*\'country_code\'', rec))
    rec = rec[18:-19]
    print('Zip Code: ' + rec)


def get_isp(ip):
    gi = pygeoip.GeoIP('GeoIPISP.dat')
    rec = str(gi.isp_by_addr(ip))
    print('ISP: ' + rec)


def get_org(ip):
    gi = pygeoip.GeoIP('GeoIPOrg.dat')
    rec = str(gi.org_by_addr(ip))
    if rec != 'None':
        print('ORG: ' + rec)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if re.findall('^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$', sys.argv[1]):
            try:
                get_info(sys.argv[1])
            except pygeoip.GeoIPError:
                print('A GeoIPError has Occurred.\nExiting program')
                exit(1)
