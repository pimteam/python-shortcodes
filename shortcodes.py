# WordPress-like Shortcodes for Python
import re, shlex

class Shortcodes:
	# we need to register the shortcodes before do_shortcode() calls
	# call do add_shortcode(shortcode, callback)
	registered_shortcodes = {}
	 
	def __init__(self):
		pass	
		
	# registers the shortcode in registered_shortcodes	
	@classmethod
	def add_shortcode(cls, shortcode, callback):
		# validate the shortcode name or raise exception
		m = re.match(r'[^A-Za-z0-9\-\_]', shortcode)		
		if re.match(r'[^A-Za-z0-9\-\_]', shortcode) is not None:
			raise ValueError('The shortcodes can contain only letters, numbers, dash and underscore')
		
		# register		
		cls.registered_shortcodes[shortcode] = callback
		
		
	# actually parses content for shortcodes	
	@classmethod
	def do_shortcode(cls, content):		
		if not len(cls.registered_shortcodes):
			return content
		
		for shortcode, callback in cls.registered_shortcodes.items():
			atts = None
			enclosed_content = ''
			sc = shortcode.replace('-','\-') # regexp-friendly version of the shortcode
			
			# find all occurrences of the shortcode with regexp
			
			# enclosing shortcodes	
			pattern =  r'\[' + shortcode + '.*?\[/' + sc + '\]+'
			enclosing_matches = re.findall(pattern, content)
			#print(len(enclosing_matches))
			
			# non-enclosing shortcodes
			pattern = r'\[' + sc + '.*?\]'		
			matches = re.findall(pattern, content)
			
			matches = enclosing_matches + matches
			
			for m in matches:
				if " " in m:
					atts, enclosed_content = cls.parse_atts(shortcode, m)
			
				try:					
					replacement = callback(atts, enclosed_content)
					content = content.replace(m, replacement)
				except:
					pass
					
		# after parsing all shortcodes		
		return content		
		# end do_shortcode()
	
	# parses the attributes in the shortcode	
	@classmethod
	def parse_atts(cls, shortcode, m):
		#print(shortcode)	
		enclosed_content = ''			
		# if there is enclosed content, we need to break on it and remove the closing shortcode	
		if '[/' + shortcode + ']' in m:
			parts = m.split(']')
			enclosed_content = parts[1].replace('[/' + shortcode, '') # get the contents and remove the closing part
			m = parts[0] + ']' # return back the m to be the same as in non-enclosed shortcode. 
		
		#print(m)
		atts = None		
		try:
			atts = m.replace('[', '').replace(']', '')			
			atts = shlex.split(atts)
			atts.pop(0) # remove the shortcode itself		
			atts = [x.split('=') for x in atts if x]		
			atts = {x[0]: x[1].replace('"','') for x in atts}		
		except:
			pass			
		
		return atts, enclosed_content
		