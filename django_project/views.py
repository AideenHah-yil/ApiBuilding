import requests
import random
from django.shortcuts import render

def index(request):
  response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
  data = response.json()
  fact = data['text'] 


  #hackathon assignment
  #instructions: use this api and randomize the students
  response2 = requests.get('https://freetestapi.com/api/v1/students')
  data2 = response2.json()
  
  #to choose a random student
  random_student = random.choice(data2)
  name = random_student['name']

  r3 = requests.get('https://dog.ceo/api/breeds/image/random')
  res3 = r3.json()
  dog = res3['message']
  
  return render(request, 'templates/index.html', {'fact': fact, 'dog': dog, 'name': name})