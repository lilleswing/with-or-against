# with-or-against
Analysis on whether to walk with or against traffic

I was wondering whether it would be faster to walk with or against lights in New York so I made a little simulation to see.
Turns out it matters a lot -- Around a 30-40% difference at worst case scenarios, but depending on small implementation details going with/against can be super good or super bad.

Assumptions that are probably incorrect
1) Symmetric Lights -- that is a light is green as long as it is red.  Generally Avenue Lights are green longer than red
2) No jay-walking.  We can also account for this by extending the amount of time for green vs red.

Using the data from 5th ave and 45th we have a 45 second light with 5 second delay which would mean that you loose 11% of time by walking with traffic.
![durations_speed_3.1](/img/durations_speed_3.1.png)
![light_seconds_speed_3.1](/img/light_seconds_speed_3.1.png)

The first graphs were assuming walking at 3.1 MPH (19 minute miles).  If you raise that to 4.0 MPH (15 minute miles) All of a sudden you hit the sweet spot at 45 second lights and get huge gains.  I don't think you can say categorically it is always better because small differences in any of the variables make a big change in efficiency. Here are the graphs for 4.0 mph.

![durations_speed_4.0](/img/durations_speed_4.0.png)
![light_seconds_speed_4.0](/img/light_seconds_speed_4.0.png)

 But a good rule of thumb is if you are a fast walker to with traffic, and a slower walker go against traffic.
 ![speed_vs_time](/imt/speed_vs_time.png)
 

After this analysis I still had some questions and was hoping you would know more.
