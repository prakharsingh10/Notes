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

If we do this in the .css file

    body {
    color: blue;
    }

then whole body will be coloured as blue.

If we want h1 and h2 to be blue ang rest bogy as red then we can specify it either in the index.html page, or using inline css or another method is to specify it in .css file .
![grouping](/images/grouping.PNG)
![groupingresult](/images/groupingresult.PNG)

We can also use a fantastic approach of using the id, and then in .css file we will specify the id

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>CSS Tutorial</title>
        <link rel="stylesheet" href="./main.css" />
    </head>
    <body>
        <!--external css-->
        <h1 id="truth">Prakhar is great</h1>
        <h2 id="truth">Prakhar is great</h2>
        <p style="width: 50%;">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Reiciendis ex
        corporis natus neque cumque? Dolore debitis ex provident, autem rem
        sapiente voluptatum non? Commodi, minima in fugiat rerum assumenda
        voluptatem accusantium, deserunt nemo dicta tempore totam a esse quam
        voluptates provident explicabo error voluptate eveniet optio voluptatibus
        veritatis architecto illo.
        <h1>Prakhar is great</h1>
        </p>
    </body>
    </html>

The below code is of .css
![id](/images/id.PNG)
![id](/images/idresult.PNG)

Note that if we choose the id and style it in .css file using the id <br/>Then we cant overwrite that properties in the index ao any page .<br/>If we want to overwrite then we have to use the id for overwriting not the selectors.

![mainover](/images/mainover.PNG)
![indexover](/images/indexover.PNG)
![resultover](/images/resultover.PNG)

<!-- class eslectors -->

# #Class Selectors#<br/>

I f we want to style some of the selectors as green then <br/>
We can give them all the same id and style it in .css file, but if we do so in future we may get problem with the id, for example if we want to put label etc.<br/><br/>
So to tackle this we can use the class and use the class attribute at the time of creation of the selector.<br/>And then in .css file we will style the whole class, though it can be done by id also but it is not a good idea to give all of them the same id.<br/><br/>
We can provide multiple class to any selectors just by seperating them by a space while creating the selectors.
![mainclass](/images/mainclass.PNG)
![indexclass](/images/indexclass.PNG)
![resultclass](/images/resultclass.PNG)

# ###DIV AND SPAN###<br/>

We can ude div and span for grouping the selectors of various kind.<br/>
With div and span we must know that div is added to the<br/> block while span is inline type.We can also add<br/>classes and ids within the div tag<br/>
Now the below code and result will give us a nice understanding about div span their combination with class and overwriting
![divspan0](/images/divspanmain.PNG)
![divspan1](/images/divspanindexn.PNG)
![divspan2](/images/divspanresult.PNG)

If we do div instead of span in the above index page then the change will be<br/> there but all the text inside the div tag will be started from the new line<br/> in the result page.

# ##Inheritance in CSS##<br/>

The concept of inheritance is very simple that whatever <br/>property is given to the parent element is going <br/> to be inherited by the child element unless property <br/> of child is specifically mentioned.
<br/><br/>
The property of parent selectors will be inherited unless <br/> we overwrite that property for the child .

![inheritance0](/images/inheritancemain.PNG)
![inheritance1](/images/inheritanceindex.PNG)
![inheritance2](/images/inheritanceresult.PNG)

Also note that if we add border in div in .css file then heading and para both <br/> wont be bordered.<br/>
LAST RULE:- If we style the paragrsph in a ceretain way in .css file and <br/>
then style the para again in the .css file with another style then the style <br/> which has last been added will be choosed as the style of the selector or <br/> para in this case.<br/><br/>
SPECIFICITY :- <br/>
IF in .css file we style the paragraph as color red, and then <br/> we madee a class green and provide the green class <br/> to a para, then the para will be green in color.<br/><br/>

# ####Universal Selector

There is a thing called universal selector which is quiet useful if we want <br>
to create certain style to our whole page or maximum page or provide certain
<br/>property to maximum selectors, then we can make use of universal selector

![universalselector](/images/universalselector.PNG)

Universal selectors have least amount of specificity.

# #COLOR PROPERTIES

RGB (value1,value2,value3) <br/>
All the values should be less than or equal to 255

![RGB](/images/rgbresult.PNG)

We can also use rgba(value1,value2,value3,factor)
<br/> And the value of factor will lie between 0 to 1.<br/>
for example we use rgba(0,0,0,0.5) then it will display somewhat gray color.<br/>
if we choose the value of factor as 0 then it will show white color

![rgbaresult](/images/rgbaresult.PNG)

# ####HEX COLORS

These are very useful and we can select them by #......
<br/> Six values are there denoting RRBBGG
<br/> we can get cool colors from "coolors.co"

# #CSS Units

1 => Pixel or px <br/>

![pixels](/images/pixelsresult.PNG)
It is considered as absolute unit, meaning that if we increse<br/> the size of the window the size of text and all other <br/> size given in pixel unit will remain same.<br/>
Note that the height and the width attributes doesn't affect the size of the text, rather they will affect the wrapping of the text.<br/>

2 =>PERCENTAGE<br/>
It is a relative unit.In the below example we created a block div and in .css file we specified this div's class and give property to the class.Then we created two more div and gave them class as well and style te class and its propeerty in .css file.See how the block gets occupied in the outer div as we create more div inside it.

![toughone](understandingpercentageindex.PNG)
![toughone2](understandingpercentageresult.PNG)
