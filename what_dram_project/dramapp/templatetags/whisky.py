from dramapp.models import Rating

def do_if_rated(parser, token):
	bits = token.contents.split()
	if len(bits) !=3:
		raise template.TemplateSyntaxError("%s tag takes two arguments" % bits[0])
	nodelist_true = parser.parse(('else', 'endif_rated'))
	token = parser.next_token()
	if token.contents == 'else':
		nodelist_false = parser.parse(('endif_rated'))
		parser.delete_first_token()
	else:
		nodelist_false = template.Nodelist()
	return IfRateNode(bits[1], bits[2], nodelist_true, nodelist_false)

class IfRatedNode(template.Node):
	def __init__(self, user, whisky, nodelist_true, nodelist_false):
		self.nodelist_true = nodelist_true
		self.nodelist_false = nodelist_false
		self.user = template.Variable(user)
		self.whisky = template.Variable(whisky)

	def  render(self, context):
		try:
			user = self.user.resolve(context)
			whisky = self.whisky.resolve(context)
		except template.VariableDoesNotExist:
			return ''
		if Rating.objects.filter(user__pk=user.id,
								whisky__pk=whisky.id):
			return self.nodelist_true.render(context)
		else:
			return self.nodelist_false.render(context)

register.tag('if_rated', do_if_rated)

def do_get_rating(parser, token):
	bits = token.contents.split()
	if len(bits) !=5:
		raise template.TemplateSyntaxError("%s tag takes for arguments" % bits[0])
	if bits[3] != 'as':
		raise template.TemplateSyntaxError("Third argument to %s must be 'as'" % bits[0])
		return GetRatingNode(bits[1], bits[2], bits[4])

class GetRatingNode(template.Node):
	def __init__(self, user, whisky, varname):
		self.user =template.Variable(user)
		self.whisky = template.Variable(whisky)
		self.varname = varname

	def render(self, context):
		try:
			user = self.user.resolve(context)
			whisky = self.whisky.resolve(context)
		except template.VariableDoesNotExist:
			return ''
		rating = Rating.objects.get(user__pk=user.id,
									whisky__pk=whisky.id)
		context[self.varname] = rating
		return ''
		
register.tag('get_rating', do_get_rating)

