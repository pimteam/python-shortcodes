# Python Shortcodes
## WordPress-style shortcodes for Python

Create and use WordPress-style shortcodes in your Python based app.

## Example
    # static output
    def my_function(atts = None, enclosed_content = ''):
        return "Output of my function"
    
    # using attributes and enclosed content (pretty simple example)    
    def tags_around(atts = None, enclosed_content = ''):
        tag = atts['tag']
        return '<' + tag + '>' + enclosed_content + '</' + tag + '>'
    
    Shortcodes.add_shortcode('my-function', my_function)
    Shortcodes.add_shortcode('tags-around', tags_around)
    
    content = """Testing: [my-function]. This will be [tags_around tag="b"]bold[/tags_around]."""
    print(Shortcodes.do_shortcodes(content))
    
    # will generate output:
    Testing: Output of my function. This will be <b>bold</b>.

## Why Use Them?

Just have a look at how powerful [WordPress shortcodes](https://wordpress.com/support/shortcodes/) are. This simple library is giving you the most improtant functionality to use in your Python projects, in Flask or Django apps, any Python based CMS, etc.

Just think about all the possibilities you are giving to the users of your app: admins, editors, or even end users can use powerful, defined by you functions to add all kind of output to user generated content, in widgets, etc.

The shortcodes are most often used in CMS-es to allow authors or editors to include powerful functionality anywhere on the site. You can have shortcodes to create contact forms, quizzes, product lists, dynamic reports - basically everything.

## Documentation
1. You can simply copy the library in a working folder and import:
    <code>from shortcodes import Shortcodes</code>
    
2. Create your custom shortcode functions. Each shortcode function or a class method should accept two optional parameters: atts and enclosed_content

Example:
    <pre><code># accepts name in enclosed content and capitalizes first letter	
    def ucfirst(atts = None, enclosed_content = ''):	
	    s = enclosed_content	
	    if s == '':
		return '' # if no enclosed content this shortcode returns nothing
	    s = s[0].upper() + s[1:]
	    return atts['add_text'] + ' ' + s</code></pre>

The function should not have side effects and must return the content. The returned content will replace the shortcode inside your content after calling Shortcodes.do_shortcode() on it. See step 4.

3. Each shortcode needs to be regusrered with add_shortcode call.
Example:
           <code>Shortcodes.add_shortcode('ucfirst', ucfirst)</code>

Unlike in WordPress, in Python you need to send the function object, and not a string with the function name. 

4. Finally, call Shortcodes.do_shortcodes() on your content to have all shortcodes replaced with the output of the associated function:
        <code>Shortcodes.do_shortcode(content)</code>

5. Shortcodes can contain named parameters with their values enclosed in double quotes. Example:
    <code>[show-time format="%H:%M:%S"]</code>
    In this example the shortcode function will receive parameter "format" with value %H:%M:%S

6. Shortcodes can enclose content like this <code>[my-shotcode param1="param 1" param2="param 2"]My content[/my-shortcode]</code>
The content will be passed a second argument to your shortcode function, this allowing you to modify it and return it.

Invalid sortcodes will be ignored and just returned in the content.

Have a look at example.py for several use cases and examples. Run it from terminal by calling
    <code>python example.py</code>

## License

[MIT](https://opensource.org/licenses/MIT)