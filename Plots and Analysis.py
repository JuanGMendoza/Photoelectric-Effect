"""This Program generates all the plots used in the paper"""

import numpy
import matplotlib.pyplot as pyplot
import os


def line(m, x , b):
    return (slope * x) + b


def stdCheck():
    
    waveLen = ('365', '404', '546' , '577', '671', '691' , '708')
    for i in range(0,7):

        data = numpy.transpose(numpy.loadtxt(waveLen[i] + 'Average.txt'))

        potential = data[0]
        current = data[1]
        uncer = data[2]

        coef = numpy.polyfit(potential[200:340], current[200:340], 0)
        
        
        neweq = numpy.poly1d(coef)
        lineData = neweq(potential)

        for k in range(0, len(potential)):
            if(current[k] > coef + (10*uncer[k])):
                break

        print('stopping V for ' + waveLen[i] + 'at:', potential[k])
        
 
        pyplot.scatter(potential[k],current[k], s = 20, label='Stopping V')
        pyplot.plot(potential, lineData, label = 'Linear Fit')
        pyplot.errorbar(potential, current,uncer, label = 'Current' )
        pyplot.legend()
        pyplot.xlim(-3,0)
        pyplot.xlabel('Accelerating Voltage (V)')
        pyplot.ylabel('Current (nA)')
        pyplot.show()


def lineFit():
    waveLen = ('365', '404', '546' , '577', '671', '691' , '708')

    for i in range(0,7):

        data = numpy.transpose(numpy.loadtxt(waveLen[i] + 'Average.txt'))

        potential = data[0]
        current = data[1]
        uncer = data[2]

        coef = numpy.polyfit(potential[200:340], current[200:340], 0)
        #print(data)
        
        neweq = numpy.poly1d(coef)
        lineData = neweq(potential)
      
        coef1 = numpy.polyfit(potential[440:455],current[440:455],1)
        neweq1 = numpy.poly1d(coef1)
        lineData1 = neweq1(potential)


       
        stopV = (coef - coef1[1])/coef1[0]
        stopVhigh = ((coef )-(coef1[1]))/coef1[0]
        print('stopping V for ' + waveLen[i] + ' at:', stopV)
        
        pyplot.scatter(stopVhigh,lineData[0])
        
        pyplot.plot(potential, lineData, label = 'No Current Fit')
        pyplot.errorbar(potential, current ,uncer, label = 'Current')
        pyplot.plot(potential, lineData1, label = 'Current Increase Fit')
        pyplot.legend()
        pyplot.ylim(-.3,1)
        pyplot.xlim(-2.5,0.2)
        pyplot.xlabel('Accelerating Voltage (V)')
        pyplot.ylabel('Current (nA)')
        pyplot.show()

def noise():

    data = numpy.transpose(numpy.loadtxt('wonky.txt'))
    data1 = numpy.transpose(numpy.loadtxt('708Average.txt'))
    pyplot.plot(data[0], data[1],label = 'Human Motion Nearby')
    pyplot.plot(data1[0], data1[1], label = '708nm Data')
    pyplot.legend()
    pyplot.xlabel('Accelerating Voltage (V)')
    pyplot.ylabel('Current (nA)')
    pyplot.xlim(-9.5,-7)
    pyplot.ylim(-.05,0.02)
    pyplot.show()

def IntensityPlot():

    directory = os.path.dirname(os.path.realpath(__file__))

   
    for filename in os.listdir(directory):
        
        if('ODAverage' in filename) or ('noOD' in filename):
            data = numpy.transpose(numpy.loadtxt(filename))
            j = 7
            if('.05' in filename):
                j = 8
            if('ODAverage' in filename):
                pyplot.errorbar(data[0], data[1], yerr = data[2], label = filename[3:j])
            else:
                 pyplot.errorbar(data[0], data[1], yerr = .005,label = filename[3:j])
            j = 7
    pyplot.xlabel('Retarding Potential [V]')
    pyplot.ylabel('Current [nA]')
    pyplot.xlim(-1.0,0.5)
    pyplot.ylim(-.1,1)
    pyplot.title('Normalized Light Intensity Effect on Stopping Voltage')
    pyplot.legend()
    pyplot.show()
            

