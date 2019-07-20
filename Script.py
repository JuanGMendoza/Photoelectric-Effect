# Program Script
# Description: 
#   This program takes data set files taken in the photoelectric lab
#   and creates new files with their mean and uncertainties for plotting

# Author: Juan Gonzalez De Mendoza
# Date: 02/21/19
# Revised: 
#02/21/19

#libraries used:
import numpy

def main():
    intensityDependence()
    wavelengthDependence()
# Function wavelengthDependence
# Description:
#
#   This function reads the raw data for the first part of the experiment.
#   Where we prove that the energy of the photon changes the stopping potential.

#   There are 5 sets of data for each wavelength. So I took the mean of all
#   5 Y-Values corresponding to one x-value and saved it in a new file. I
#   also included a third column in this new file which will be the uncertainty that corresponds
#   to each y value. This uncertainty comes from one standard deviation / sqrt(5) which
#   is the number of trials we did.
#   
# Calls:
#   None
# Parameters:
#   None
# Returns:
#   Nothing

def wavelengthDependence():
    letter = ('a', 'b', 'c' , 'd', 'e')
    waveLen = ('365', '404', '546' , '577', '671', '691' , '708')
    tempY = ['','','','','']
    newData = numpy.zeros(3)
    data = dict()
    for i in range(0,7):
        
        for j in range(0,5):
            
        
            data[j] = numpy.loadtxt(waveLen[i] + letter[j] + '.txt')
            newFile = open(waveLen[i] + 'Average.txt', 'w')
        for x in range(0, len(data[0])):
            
            newData[0] = data[0][x][0]
            
            for k in range (0,5):
                tempY[k] = data[k][x][1]
                
            newData[1] = numpy.mean(tempY)
            newData[2] = numpy.std(tempY)
            newFile.write(str(newData[0]) + ' ' + " {:.5f}".format(newData[1]) + ' ' + " {:.5f}".format(newData[2]) + '\n')
        newFile.close()


# Function wavelengthDependence
# Description:
#
#   This function reads the raw data for the second part of the experiment.
#   Where we prove that the intensity of the light source does not affect the
#   stopping potential. Which agrees with quantization of light.

#   Did exactly the same thing as the function above but with different file names
#   
# Calls:
#   None
# Parameters:
#   None
# Returns:
#   Nothing

def intensityDependence():
    letter = ('a', 'b', 'c' , 'd', 'e')
    ODs = ('.05', '.3', '.5', '.7', '1')
    tempY = ['','','','','']
    newData = numpy.zeros(3)
    data = dict()
    for i in range(0,5):
        
        for j in range(0,5):
            
        
            data[j] = numpy.loadtxt('546' + ODs[i] + 'OD' + letter[j] + '.txt')
           
            newFile = open('546' + ODs[i] + 'ODAverage.txt', 'w')
        for x in range(0, len(data[0])):
            
            newData[0] = data[0][x][0]
            
            for k in range (0,5):
                tempY[k] = data[k][x][1]
            
            newData[1] = numpy.mean(tempY)
            newData[2] = numpy.std(tempY)
            newFile.write(str(newData[0]) + ' ' + " {:.5f}".format(newData[1]) + ' ' + " {:.5f}".format(newData[2]) + '\n')
        newFile.close()



main()



    
