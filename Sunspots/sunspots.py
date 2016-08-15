from urllib import urlopen
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderPDF

url = 'http://services.swpc.noaa.gov/text/predicted-sunspot-radio-flux.txt'