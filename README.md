# Find Me In Freetown Web Application

Built using Flask and HTML/CSS/JS

- Users can visit the app at findmeinfreetown.com

- They are met with an interactive Google Map, with an overlay of the 47 wards in Freetown

- When clicking on one of the wards, a popup appears with a link to that ward's page on the Freetown City Council website ( which I also helped build )

- Users can click the geolocation button, which triggers HTML5 geolocation. If a set of coordinates are found, they are sent via AJAX to the Flask API, which checks which ward the user is in, using the geopandas Python module.

- If the user is in a ward, the map pans to said ward and a pin appears showing the users position inside the ward. A link also appears which takes users to the page for that ward on the Freetown City Council website.


You can find out more on [my webiste](https://www.oliveriyer.com/freetown-city-council-find-me-in-freetown/).
