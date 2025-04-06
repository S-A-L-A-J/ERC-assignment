# ERC-assignment
In this assignment, we are given an AM signal which means Amplitude Modulation. What actually is happening here is that we are getting a sound wave at a certain frequency, which is the original frequency at which it is recorded. To mask or shadow this sound wave we are using Amplitude Modulation, which means to wrap this signal with a wave which is at a much higher frequency, due to this we are not able to directly hear the audio message. Some applications which i can think of this are maybe this is used in encrypting messages in military. They apply a certain frequency filter while encoding the message and their teammates who are recieving the message only know which filter was used and they can convert the AM signal back to the real message. 

In terms of technical detials, we are first converting the AM signal to a usable format in our code by using scipy.io to make it into a signal. We then proceed to convert it into a normalized form, which just means dividing each value by the absolute maximum value. Then we apply the fourier transform which gives us how much of each frequency is in the signal and also gives the matching frequency values. These values which we obtain are symmetric so we then proceed to take only the positive part of the frequncy distribution. Visualizing this graph using matplotlib we get the following graph : 

![image](https://github.com/user-attachments/assets/43dd2101-d093-4f62-897b-dc8668fac7ee)

We get two peaks in this graph, they correspond to two different values where the value of frequency are coming the maximum number of times. Let's say the carrier frequency is F and the actual message frequency is f, then the two peaks are for F-f and F+f. To get the carrier frequency, we take the mean and get F. Now using demodulation by using modulated_wave * cos(2*pi*F*time) we get the demodulated wave. I got the wave which sounds like a bird. 
I tried changing different varieties of filters, changing the cutoff frequency to varying values, using different ways to calculate the carrier frequency, like i tried to zoom into the graph in matplotlib and found the visual value of frequency upto two decimal places, i also tried applying a low pass filter, and tweaked a lot of values to find a better audio but this was the best i could get. 

Here is the graph of both the waves together, when i applied the low pass filter, it gives a clean single wave with low frequency but the sound was no better that's why i chose this graph : 

![image](https://github.com/user-attachments/assets/41dcf807-e858-4aea-936b-3a86ef549968)

