from shortcodes import Shortcodes as s

# simply displays hello world or hello name
def hello_world(atts = None, enclosed_content = ''):	
	if atts is None or 'name' not in atts: 
		return "Hello, world"
	else: 
		return f"Hello {atts['name']}"
	# end hello_world

# accepts name in enclosed content and capitalizes first letter	
def ucfirst(atts = None, enclosed_content = ''):	
	s = enclosed_content	
	if s == '':
		return '' # if no enclosed content this shortcode returns nothing
	s = s[0].upper() + s[1:]
	
	return atts['add_text'] + ' ' + s
	# end ucfirst
	
# basic function to print time. We will not validate the parameter passed to the python function
def show_time(atts = None, enclosed_content = ''):
	from datetime import datetime

	now = datetime.now()
	format = atts['format'] if atts is not None and 'format' in atts else '%H:%M'

	current_time = now.strftime(format)
	return current_time	

s.add_shortcode('hello-world', hello_world)
s.add_shortcode('ucfirst', ucfirst)
s.add_shortcode('show-time', show_time)

content = """This is some content here. Here's the shortrcode: [hello-world] and also invalid shortcode [invalid-shortcode].
Here is a shortcode with some parameters. The time is [show-time format="%H:%M:%S"   not_needed="a"].
Let's also have an shortcode enclosing some content: [ucfirst add_text="First name:"]john[/ucfirst].
Using the same once again: Hello [ucfirst add_text="Mrs."]hellen[/ucfirst].
And the now it's still [show-time format="%-I %p"]meaningless enclosed content - this function doesn't do anything with it so it will be skipped[/show-time].""" 

print(s.do_shortcode(content))