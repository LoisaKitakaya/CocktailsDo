# CocktailsDo
A Django CRUD app. Features include User Authentication, CRUD operations, Markdown Field support, Live deployment to Heroku.

[Preview live](<https://cocktailsdo.herokuapp.com/> "Live View")

## Technologies
- HTML
- CSS
- Javascript
- Django/python
- Postgresql

## Local Installation
Follow these steps if you want to install CocktailsDo locally.

```
git clone https://github.com/LoisaKitakaya/CocktailsDo && cd CocktailsDo/

# create and activate virtual environment
virtualenv env
source env/bin/activate

# install requirements
pip install -r requirements.txt

# run migrations to create database
python manage.py migrate

# run the app
python manage.py runserver
```

## Issues/Troubleshooting
The webapp might not be fully responsive on all devices, but should work fine on the standart desktop/laptop.

If you come across any bugs/issues with the code, feel free to open a [new issue](<https://github.com/LoisaKitakaya/CocktailsDo/issues>) in the repo. If you experience technical issues, you can always do a quick Google search to see if someone has encountered a similar Django-related issue before.

## Contributing
[Pull requests](<https://github.com/LoisaKitakaya/CocktailsDo/pulls>) are welcome. For major changes, please open an [issue](<https://github.com/LoisaKitakaya/CocktailsDo/issues>) first to discuss what you would like to change. Make sure to run tests and migrations as appropriate.

## License
MIT License

Copyright (c) 2021 Loisa Kitakaya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
