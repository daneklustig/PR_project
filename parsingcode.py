import pip
package_name='bs4'
pip.main(['install', package_name])
from bs4 import BeautifulSoup as soup
import csv

#define the parsing function
def parse(html_file):
  html=open(html_file).read()
  soup1=soup(html,"lxml")
  try:
    alw=soup1.find('div',{'class': "headHeadline"}).next.next.next.next.next.next.next
  except:
    alw =""
  try:
    location=soup1.find('div',{'class': "headHeadline"}).next.next.next.next.next.next.next.next.next.next
  except:
    location=""
  try:
    header=soup1.find('td',{'class': "headline"}).next
  except:
    header =""
  try:
    about=soup1.find('td',{'colspan': "2"}).next
  except:
    about =""
  try:
    profile=soup1.find('th',text='Profile number').next.next.next.next
  except:
    profile=""
  try:
    lang=soup1.find('th',text='Language').next.next.next.next
  except:
    lang=""
  try:
    body=soup1.find('th',text='Body').next.next.next.next
  except:
    body=""
  try:
    ethnicity=soup1.find('th',text='Ethnicity').next.next.next.next
  except:
    ethnicity=""
  try:
    boeth=soup1.find('th',text='Body & ethnicity').next.next.next.next
  except:
    boeth=""
  try:
    hair=soup1.find('th',text='Hair').next.next.next.next
  except:
    hair=""
  try:
    bodyhair=soup1.find('th',text='Body Hair').next.next.next.next
  except:
    bodyhair=""                  
  try:
    eyes=soup1.find('th',text='Eyes').next.next.next.next
  except:
    eyes=""
  try:
    piercings=soup1.find('th',text='Piercings').next.next.next.next
  except:
    piercings=""
  try:
    tattoos=soup1.find('th',text='Tattoos').next.next.next.next
  except:
    tattoos=""
  try:
    smoker=soup1.find('th',text='Smoker').next.next.next.next
  except:
    smoker=""
  try:
    sex=soup1.find('th',text='Sex').next.next.next.next
  except:
    sex=""
  try:
    relationship=soup1.find('th',text='Relationship').next.next.next.next
  except:
    relationship=""
  try:
    lookingfor=soup1.find('th',text='Looking for').next.next.next.next
  except:
    lookingfor="" 
  try:
    profession=soup1.find('th',text='Profession').next.next.next.next
  except:
    profession="" 
  try:
    religion=soup1.find('th',text='Religion').next.next.next.next
  except:
    religion=""
  try:
    food=soup1.find('th',text='Food').next.next.next.next
  except:
    food=""     
  try:
    music=soup1.find('th',text='Music').next.next.next.next
  except:
    music=""      
  try:
    sport=soup1.find('th',text='Sport').next.next.next.next
  except:
    sport="" 
  try:
    travel=soup1.find('th',text='Travel').next.next.next.next
  except:
    travel="" 
  try:
    nightlife=soup1.find('th',text='Night life').next.next.next.next
  except:
    nightlife="" 
  try:
    interests=soup1.find('th',text='Interests').next.next.next.next
  except:
    interests=""    
  try:
    dick=soup1.find('th',text='Dick').next.next.next.next
  except:
    dick=""    
  try:
    posit=soup1.find('th',text='Position').next.next.next.next
  except:
    posit=""    
  try:
    fucking=soup1.find('th',text='Fucking').next.next.next.next
  except:
    fucking=""    
  try:
    fisting=soup1.find('th',text='Fisting').next.next.next.next
  except:
    fisting=""  
  try:
    safesex=soup1.find('th',text='Safer Sex').next.next.next.next.next
  except:
    safesex="" 
  try:
    sandm=soup1.find('th',text='S&M').next.next.next.next
  except:
    sandm=""
  try:
    dirty=soup1.find('th',text='Dirty').next.next.next.next
  except:
    dirty=""        
  try:
    fetish=soup1.find('th',text='Fetish').next.next.next.next
  except:
    fetish=""    
  with open ('romeo_test1.csv','a') as f:
    writer=csv.writer(f, delimiter = ';')
    writer.writerow((profile,alw,location,lang,body,ethnicity,boeth,hair,bodyhair,eyes,piercings,tattoos,smoker,sex,relationship,lookingfor,profession,religion,food,music,sport,travel,nightlife,interests,dick,posit,fucking,fisting,safesex,sandm,dirty,fetish,header,about))

#import library important for navigation between directories
import os

#change to your working directory (folder with downloaded profiles)
os.chdir("C:/Users/admin/Dropbox/HWR/BIPM/02 Semester/EA for Big Data/Project/Parsing")
os.getcwd()

#write a loop that iterates over the files in the working directory
for html_file in os.listdir("C:/Users/admin/Dropbox/HWR/BIPM/02 Semester/EA for Big Data/Project/Parsing"):
    if html_file.startswith("new"):
        parse(html_file)
        continue
    else:
        continue
