=> WE CAN ALSO CREATE TABLE IN OUR WEBPAGE

    <body>
     <table>
      <tr>
       <th>Name</th>
       <th>Age</th>
       <th>Class</th>
      </tr>
      <tr>
       <td>Prakhar</td>
       <td>19</td>
       <td>11</td>
      </tr>
     </table>
    </body>

![Table creation with heading](/images/table.PNG)

WE CAN ALSO INSERT FORM IN OUR WEBPAGE

    <body>
     <form action="">

      <input type="text" name="name" id="">
      <br>
      <input type="submit">

     </form>
    </body>

for creating the button we can also use the button element

    <body>
     <form action="">

      <input type="text" name="name" id="">
      <br>
      <button type="submit">bhar lo</button>

     </form>
    </body>

WE CAN USE THE ID FOR THE LABEL

    <body>
     <form action="">
      <label for="don">Please Enter Your Name</label>
      <input type="text" name="name" id="don">
      <br>
      <button type="submit">bhar lo</button>

     </form>
    </body>

![form-with-label](/images/formwithbottonandlabel.PNG)

    <body>
     <form action="">
      <label for="don">Please Enter Your Name</label>

      <input type="text" name="name" placeholder="name" id="don">
      <br>
      <label for="mail">Enter your email-id</label>
      <input type="email" value="email@xyz" id = "mail">
      <br>
      <label for="guptnumber">Enter your guptnumber</label>
      <input type="password" placeholder="password" id ="guptnumber">
      <br>
      <button type="submit">bhar lo</button>

     </form>
    </body>

The above code will generate following thing
![New form image](/images/newform.PNG)

WE CAN ALSO INTRODUCE SOME TEXTAREA IN OUR WEBPAGE

    <body>
    <form action="">
    <label for="don">Please Enter Your Name</label>

    <input type="text" name="name" placeholder="name" id="don">
    <br>
    <label for="mail">Enter your email-id</label>
    <input type="email" value="email@xyz" id = "mail">
    <br>
    <p>About this website</p>
    <textarea name="" id="" cols="30" rows="10">Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto eveniet, aliquam dolorum fugiat nulla fugit ducimus molestias laborum voluptas? Qui molestiae rerum modi neque adipisci asperiores distinctio quis commodi in!</textarea>
    <br>
    <label for="guptnumber">Enter your guptnumber</label>
    <input type="password" placeholder="password" id ="guptnumber">
    <br>
    <button type="submit">bhar lo</button>

    </form>
    </body>

![textarea](/images/textarea.PNG)

#RADIO BUTTONS :-
We can also insert radio button which will allow the user to choose certain info, we can do this by

    <p>Select your fav pragraming language</p>
    <input type="radio" name="lang" id="chutiya hai">JAVA
    <input type="radio" name="lanqg" id="smart hai">Python
    <input type="radio" name="lang" id="baccha hai">C/C++
    <input type="radio" name="lang" id="thik thak">Javascript
    <br>
    <label for="guptnumber">Enter your guptnumber</label>
    <input type="password" placeholder="password" id ="guptnumber">
    <br>
    <button type="submit">bhar lo</button>

    </form>
    </body>

![radiobutton](/images/radiobutton.PNG)
In the attribute name you can see that if we have same name in two or more such radio buttons then the user will only be able to select one such radio button.In value attribute we provide the text which will be forwarded to server of database if the user select that option.And after that comes the label of that button.

#CHECKBOX
We can also have checkboxes and in checkboxes we can select more than one options.Thats how we do it:-

    <p>Select your favourite food</p>
    <input type="checkbox" name="" value="meetha" id="">Rasgulla
    <input type="checkbox" name="" value="chatpata" id="">Namkeen
    <input type="checkbox" name="" value="khatta" id="">Imli
    <br><br><br>
    <label for="guptnumber">Enter your guptnumber</label>
    <input type="password" placeholder="password" id ="guptnumber">
    <br>
    <button type="submit">bhar lo</button>

    </form>

![checkbox](/images/checkbox.PNG)
If we add checked attribute while creating checkbox,that checkbox will already be checked from the starting though we can uncheck it.

DROPDORN OR SELECT
We can create some dropdowns in our webpage

    <p>Select your favourite food</p>
    <input type="checkbox" name="" value="meetha" id="">Rasgulla
    <input type="checkbox" name="" value="chatpata" id="">Namkeen
    <input type="checkbox" name="" value="khatta" id="">Imli
    <br><br><br>
    <select name="" id="">
    <option value="xx">Girl</option>
    <option value="xy">Boy</option>
    <option value="yy">Trans</option>
    </select>
    <br>
    <label for="guptnumber">Enter your guptnumber</label>
    <input type="password" placeholder="password" id ="guptnumber">
    <br>
    <button type="submit">bhar lo</button>

    </form>
    </body>

![dropdownselect](/images/select.PNG)

![savetime](/images/savetime.PNG)

                   CSS - CASCADING STYLE SHEETS

It is responsible for styling the web  
selector{property:value;property:value}
there are three ways to start css:
inline,internal,external

INLINE CSS:-

    <body>
        <!--inline css-->
        <h1 style="color: darkorange; font-size: 3rem;">Hello world</h1>
        <h2 style="color: rgb(0, 110, 255);">Prakhar is great</h2>
    </body>

![inlinecss](/images/inlinecss.PNG)

However we note that if we want to colour red multiple headings then we have type it again and again in inline css.To encounter that we use internl css.

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>CSS Tutorial</title>
        <style>
        h1 {
            color: red;
            font-size: 3rem;
        }
        h2 {
            color: seagreen;
            font-size: 1rem;
        }
        </style>
    </head>
    <body>
        <!--internal css-->
        <h1>Prakhar is great</h1>
        <h1>Prakhar is great</h1>
        <h1>Prakhar is great</h1>
        <h1>Prakhar is great</h1>
        <h2>Prakhar is great</h2>
    </body>
    </html>

In internal css we added the style in the head tag and we specified the properties of all the h1,h2 element inside the newly created style tag in head.

![internal css](/images/internalcss.PNG)
And if we want lets say one heading to be differently styled then we caan use inline css in that heading.It will get preference over the iinternal css.

In internall css we were lacking the flexibility for the multiple pages.TO tackle this we can use external css.
We created a .css file in our workspace and then put all our css styles into that .css file.Then we provide link of css into head tag in index,html,about.html and all the pages we want to style.

![maincss](/images/maincss.PNG)
![INDEXCSS](/images/indexcss.PNG)
![ABOUTCSS](/images/aboutcss.PNG)
s
