# ERC-assignment
In this assignment, we are given an AM signal which means Amplitude Modulation. What actually is happening here is that we are getting a sound wave at a certain frequency, which is the original frequency at which it is recorded. To mask or shadow this sound wave we are using Amplitude Modulation, which means to wrap this signal with a wave which is at a much higher frequency, due to this we are not able to directly hear the audio message. Some applications which i can think of this are maybe this is used in encrypting messages in military. They apply a certain frequency filter while encoding the message and their teammates who are recieving the message only know which filter was used and they can convert the AM signal back to the real message. 

In terms of technical detials, we are first converting the AM signal to a usable format in our code by using scipy.io to make it into a signal. We then proceed to convert it into a normalized form, which just means dividing each value by the absolute maximum value. Then we apply the fourier transform which gives us how much of each frequency is in the signal and also gives the matching frequency values. These values which we obtain are symmetric so we then proceed to take only the positive part of the frequncy distribution. Visualizing this graph using matplotlib we get the following graph : 

![image](https://github.com/user-attachments/assets/43dd2101-d093-4f62-897b-dc8668fac7ee)

![image](https://github.com/user-attachments/assets/32b30de2-83b1-4943-8a5c-4f7ebe411cf1)

