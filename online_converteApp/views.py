from django.shortcuts import render
import django.core.exceptions 
from fractions import Fraction
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.gis.measure import D, Distance
from measurement.measures import Weight, Volume
import statistics
import math
import random,sys
#from .how_long_is_it import Long
def home(request):
	return render(request,'base.html')
def fraction(request):
	if request.method == 'POST':
		decimal_value = request.POST['decimal_value']
		try:
			decimal_result = Fraction(decimal_value)
			return render(request,'fraction.html',{'decimal_result': decimal_result})
		except Exception as e:
			e.message = 'Please Enter Correct Number'
			return render(request,'fraction.html',{'message': e.message})
		#print(decimal_value)
	return render(request,'fraction.html')

def factorial(request):
	if request.method == 'POST':
		value = [(x) for x in request.POST['factorial'].split()]
		#print(value)
		
		try:
			factorial_result = []
			for n in value:
				#l = math.factorial(n)
				factorial_result.append(math.factorial(int(n)))
				#print(factorial_result)
			return render(request,'factorial.html',{'factorial_result': factorial_result})
		except (ValueError,AssertionError):
			message = 'Please Enter Correct Number'
			return render(request,'factorial.html',{'message': message})

	return render(request,'factorial.html')

def how_long_is_it(request):
	if request.method == 'POST':
		long_value = request.POST['long']
		select = request.POST['select']

		try:

			if select == 'Foot':
				cvalue = D(ft=long_value)
				r = [cvalue.ft,'Foot'], [cvalue.km,'Kilometer'], [cvalue.mi,'Mile'], \
				[cvalue.cm,'Centimeter'], [cvalue.m,'Meter'], [cvalue.yd,'Yard'], [cvalue.inch,'inches']
				return render(request,'how_long_is_it.html',{'r':r})

			elif select == 'Kilometer':
				cvalue = D(km=long_value)
				r = [cvalue.ft,'Foot'], [cvalue.km,'Kilometer'], [cvalue.mi,'Mile'], \
				[cvalue.cm,'Centimeter'], [cvalue.m,'Meter'], [cvalue.yd,'Yard'], [cvalue.inch,'inches']
				return render(request,'how_long_is_it.html',{'r':r})

			elif select == 'Mile':
				cvalue = D(mi=long_value)
				r = [cvalue.ft,'Foot'], [cvalue.km,'Kilometer'], [cvalue.mi,'Mile'], \
				[cvalue.cm,'Centimeter'], [cvalue.m,'Meter'], [cvalue.yd,'Yard'], [cvalue.inch,'inches']
				return render(request,'how_long_is_it.html',{'r':r})

			elif select == 'Centimeter':
				cvalue = D(cm=long_value)
				r = [cvalue.ft,'Foot'], [cvalue.km,'Kilometer'], [cvalue.mi,'Mile'], \
				[cvalue.cm,'Centimeter'], [cvalue.m,'Meter'], [cvalue.yd,'Yard'], [cvalue.inch,'inches']
				return render(request,'how_long_is_it.html',{'r':r})

			elif select == 'Meter':
				cvalue = D(m=long_value)
				r = [cvalue.ft,'Foot'], [cvalue.km,'Kilometer'], [cvalue.mi,'Mile'], \
				[cvalue.cm,'Centimeter'], [cvalue.m,'Meter'], [cvalue.yd,'Yard'], [cvalue.inch,'inches']
				return render(request,'how_long_is_it.html',{'r':r})

			elif select == 'Yard':
				cvalue = D(yd=long_value)
				r = [cvalue.ft,'Foot'], [cvalue.km,'Kilometer'], [cvalue.mi,'Mile'], \
				[cvalue.cm,'Centimeter'], [cvalue.m,'Meter'], [cvalue.yd,'Yard'], [cvalue.inch,'Inches']
				return render(request,'how_long_is_it.html',{'r':r})

			elif select == 'Inche':
				cvalue = D(inch=long_value)
				r = [cvalue.ft,'Foot'], [cvalue.km,'Kilometer'], [cvalue.mi,'Mile'], \
				[cvalue.cm,'Centimeter'], [cvalue.m,'Meter'], [cvalue.yd,'Yard'], [cvalue.inch,'Inches']
				return render(request,'how_long_is_it.html',{'r':r})
		except ValueError:
			m = 'Please Enter Correct Number'
			return render(request,'how_long_is_it.html',{'m':m})
	return render(request,'how_long_is_it.html')

def weigh(request):
	if request.method == 'POST':
		value = request.POST['values']
		select = request.POST['select']
		try:

			if select == 'grams':
				cvalue = Weight(g=value)
				print(cvalue)
				r = [cvalue.kg,'Kilograms'], [cvalue.g,'Grams'], [cvalue.lb,'Pounds'], \
				[cvalue.oz,'Ounces'], [cvalue.tonne,'Tons']
				return render(request,'How_much_does_it_weigh.html',{'r':r})

			elif select == 'kilograms':
				cvalue = Weight(kg=value)
				r = [cvalue.kg,'Kilograms'], [cvalue.g,'Grams'], [cvalue.lb,'Pounds'], \
				[cvalue.oz,'Ounces'], [cvalue.tonne,'Tons']
				return render(request,'How_much_does_it_weigh.html',{'r':r})

			elif select == 'ounces':
				cvalue = Weight(oz=value)
				r = [cvalue.kg,'Kilograms'], [cvalue.g,'Grams'], [cvalue.lb,'Pounds'], \
				[cvalue.oz,'Ounces'], [cvalue.tonne,'Tons']
				return render(request,'How_much_does_it_weigh.html',{'r':r})

			elif select == 'pounds':
				cvalue = Weight(lb=value)
				r = [cvalue.kg,'Kilograms'], [cvalue.g,'Grams'], [cvalue.lb,'Pounds'], \
				[cvalue.oz,'Ounces'], [cvalue.tonne,'Tons']
				return render(request,'How_much_does_it_weigh.html',{'r':r})

			elif select == 'tons':
				cvalue = Weight(tonne=value)
				r = [cvalue.kg,'Kilograms'], [cvalue.g,'Grams'], [cvalue.lb,'Pounds'], \
				[cvalue.oz,'Ounces'], [cvalue.tonne,'Tons']
				return render(request,'How_much_does_it_weigh.html',{'r':r})
		except ValueError:
			m = '''Can't Be Convert It.....'''
			return render(request,'How_much_does_it_weigh.html',{'m':m})

	return render(request,'How_much_does_it_weigh.html')

def mmmv(request):
	if request.method == 'POST':
		value = [(x) for x in request.POST['value'].split()]
		print(value)
		l = []
		try:
			for i in value:
				l.append(int(i))
		except (ValueError):
			m = 'No unique mode; Found 2 equally common values or (#Sring Values!)'
			return render(request,'Mean_Median_mode_and_Variance.html',{'m': m})
		try:
			reslut = 'Mean: ' ,statistics.mean(l)
			reslut1 = 'Median: ' ,statistics.median(l)
			reslut2 = 'Mode: ' ,statistics.mode(l)
			reslut3 = 'Variance: ' ,statistics.variance(l)
			
			c = [reslut, reslut1, reslut2, reslut3]
			return render(request,'Mean_Median_mode_and_Variance.html',{'c': c})
		except statistics.StatisticsError as e: # For know to,how to showing build in Errors
			m = e # For know to,how to showing build in Errors
			return render(request,'Mean_Median_mode_and_Variance.html',{'m': m})
	return render(request,'Mean_Median_mode_and_Variance.html')

def random_no(request):
	if request.method == 'POST':
		n = []
		total_number       = int(request.POST['total_number'])
		lower_limit_number = int(request.POST['lower_limit_number'])
		upper_limit_number = int(request.POST['upper_limit_number'])
		for i in range(3):
			if len(str(total_number)) > 5:
				m = 'Invalid Values....(Limits)'
				return render(request,'random_no.html',{'e': m})
			elif len(str(lower_limit_number)) > 5:
				m = 'Invalid Values....(Limits)'
				return render(request,'random_no.html',{'e': m})
			elif len(str(upper_limit_number)) > 5:
				m = 'Invalid Values....(Limits)'
				return render(request,'random_no.html',{'e': m})
		try:
			for i in range(0,total_number): # generates 44 random integer values between 0 and 44.
		   		r = random.randint(lower_limit_number,upper_limit_number) #integer values between 2 and 44.
		   		n.append(r)
			return render(request,'random_no.html',{'n': n})
		except Exception as e:
			e.m = 'Invalid Values....(Limits)'
			return render(request,'random_no.html',{'e': e.m})
	return render(request,'random_no.html')