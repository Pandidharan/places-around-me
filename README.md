# Places Around Me
## AIM:
To develop a website to display details about the places around my area.

## Design Steps:

### Step 1:
Take a screenshot of satellite image of your surrounding area.Chosse 5 different places around you.

### Step 2:
Create a new project and a app for your project.Create templates for your web application to display image and to use image mapping function.

### Step 3:
Now write the appropiate html code using map tag for your image to choose the places you wish to describe about.Then create templates for each place that you have chosen.

### Step 4:
Then create appropiate views for your templates and provide the urls for them in urls.py.Now run the server to use your web application and see the result.
## Code:
```
<!DOCTYPE html>
<html>
    <head>
        <title>Koyambedu market Map</title>
    </head>
    <body>
        <h1 align='center'> Map of koyambedu market and it's surrounding area</h1>
        <h2  align='left'>Address:</h2>
        <h3 align='left'>Wholesale Market Complex, Koyambedu, Chennai, Tamil Nadu 600107</h3>
        <img src="/static/images/map.png" width="1201" height="612" align='center' usemap="#image-map">
            <map name="image-map">
                <area title="Metro station" href="metro.html" shape="rect" coords="376,108,151,0">
                <area title="Vegetable market" href="vegmarket.html" shape="rect" coords="84,328,481,559">
                <area title="Sewage Treatment Plant" href="sewage.html" shape="poly" coords="757,392,840,365,880,425,861,494,836,558,816,589,776,611,696,605,639,609,652,583,707,488" >
                <area title="Flower market" href="flower.html" shape="poly" coords="489,329,518,318,766,307,637,559,488,561">
                <area title="CMBT Bus stand" href="busstand.html" shape="poly" coords="914,192,896,227,847,225,828,259,930,339,1108,353,1117,277,1012,184">
            </map>
        
</body>
</html>
```

## Output:

![Koyambedu](./2.png)
![metro](./3.png)
![vegetable market](./4.png)
![cmbt bus stand](./5.png)
![flower market](./6.png)
![sewage treatment plant](./7.png)


## Result:
Thus,a website has been successfully created to display details about the places around my area.