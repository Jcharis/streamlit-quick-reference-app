import streamlit as st

def main():
	"""Streamlit Quick Reference App 
	 For Easy Reference and Quick Ref

	 """

	raw_code_text = """
	# Title
	st.title("This is a title")
	# Header
	st.header("This is a Header")
	# Subheader
	st.subheader("This is a  sub header")

	# Text
	st.text("This is a text")

	# Markdown
	st.markdown("#### This is a Markdown ")

	"""

	raw_code_alert = """
	# Error text
	st.success("Successful")

	st.info("This is an info alert ")

	st.warning("This is a warning ")

	st.error("This shows an error ")

	st.exception("NameError('name not defined')")

	# Getting Help Info From Python
	st.help(range)

	"""
	raw_code_write = """
	# Writing Text/Super Fxn
	st.write("Text with write")

	st.write("Python Range with write",range(10))
	"""

	raw_code_media = """
	# Images
	from PIL import Image 
	img = Image.open("example.jpeg")
	st.image(img,width=300,caption='Streamlit Images')

	# Videos
	video_file = open("example.mp4",'rb')
	video_bytes = video_file.read()
	st.video(video_bytes)

	# Audio
	audio_file = open("eample.mp3",'rb')
	audio_bytes = audio_file.read()
	st.audio(audio_bytes,format='audio/mp3')

	"""

	raw_code_widget = """
	# Widget
	# Checkbox
	if st.checkbox("Show/Hide"):
		st.text("Showing or Hiding Widget")

	# Radio Button
	status = st.radio("What is your status",('Active','Inactive'))
	if status == 'Active':
		st.text("Status is Active")
	else:
		st.warning("Not Active Yet")

	# SelectBox
	occupation = st.selectbox("Your Occupation",['Data Scientist','Programmer','Doctor','Businessman'])
	st.write("You selected this option",occupation)

	# MultiSelect
	location = st.multiselect("Where do you stay",("London","New York","Accra","Kiev","Berlin","New Delhi"))
	st.write("You selected",len(location),"location")


	# Slider
	salary = st.slider("What is your salary",1000,10000)

	# Buttons
	st.button("Simple Button")

	"""

	raw_code_inputs = """
	# Text Input
	name = st.text_input("Enter Name","Type Here...")
	if st.button('Submit'):
	    result = name.title()
	    st.success(result)
	else:
	    st.write("Press the above button..")

	# Text Area
	c_text = st.text_area("Enter Text","Type Here...")
	if st.button('Analyze'):
	    c_result = c_text.title()
	    st.success(c_result)
	else:
	    st.write("Press the above button..")


	#  Date Input
	import datetime,time
	today = st.date_input("Today is",datetime.datetime.now())


	# Time Input
	t = st.time_input("The time now is",datetime.time())

	"""

	raw_code_others = """
	# SIDE Bar
	st.sidebar.header("Side Bar Header")
	st.sidebar.text("Hello")


	# Display JSON
	st.text("Display JSON")
	st.json({'name':'hello','age':34})

	# Display Raw Code
	st.text("Display Raw Code")
	st.code("import numpy as np")


	st.text("Display Raw Code Alternative Method")
	with st.echo():
		# This will also be shown
		import pandas as pd 
		df = pd.DataFrame()


	# Progress Bar
	import time
	my_bar = st.progress(0)
	for p  in range(10):
		my_bar.progress(p +1)

	# Spinner
	with st.spinner("Waiting .."):
		time.sleep(5)
	st.success("Finished!")

	# Placeholder with empty
	age = st.empty()
	age.text("Your Age")
	Replace with image
	age.image(img)


	# Cache For Performance
	@st.cache
	def run_multiple():
		return range(100)

	# Display the result of function
	st.write(run_multiple())

	# Show Balloons
	st.balloons()

	"""

	# Title
	st.title("Streamlit Quick Reference")


	# All Display  Begins Here
	if st.checkbox("Preview [Text,Header,Subheader,Markdown]"):
		# Title
		st.title("This is a title")
		# Header
		st.header("This is a Header")
		# Subheader
		st.subheader("This is a  sub header")

		# Text
		st.text("This is a text")

		# Markdown
		st.markdown("#### This is a Markdown ")


	if st.checkbox("Display Code [Text,Header,Subheader,Markdown]"):
		st.code(raw_code_text)

	### Ends Here
	### Begin Here

	if st.checkbox("Preview For [Alert,Help]"):
		# Error text
		st.success("Successful")

		st.info("This is an info alert ")

		st.warning("This is a warning ")

		st.error("This shows an error ")

		st.exception("NameError('name not defined')")

		# Getting Help Info From Python
		st.help(range)



	if st.checkbox("Display Code For [Alert,Help]"):
		st.code(raw_code_alert)

	### Ends Here
	### Begin Here

	if st.checkbox("Preview For [Write]"):
		# Writing Text/Super Fxn
		st.write("Text with write")

		st.write("Python Range with write",range(10))


		
	if st.checkbox("Display Code For [Write]"):
		st.code(raw_code_write)
	### Ends Here
	### Begin Here

	if st.checkbox("Preview For [Images,Videos,Audio]"):
		
		# Images
		from PIL import Image 
		img = Image.open("example.jpeg")
		st.image(img,width=300,caption='Streamlit Images')

		# Videos
		# video_file = open("example.mp4",'rb')
		# video_bytes = video_file.read()
		# st.video(video_bytes)

		# Audio
		# audio_file = open("example.mp3",'rb')
		# audio_bytes = audio_file.read()
		# st.audio(audio_bytes,format='audio/mp3')



	if st.checkbox("Display Code For [Images,Videos,Audio]"):
		st.code(raw_code_media)

	### Ends Here
	### Begin Here
	if st.checkbox("Preview For Widget [Checkbox,Radio Button,SelectBox,MultiSelect,Button,Slider]"):
		# Widget
		# Checkbox
		if st.checkbox("Show/Hide"):
			st.text("Showing or Hiding Widget")

		# Radio Button
		status = st.radio("What is your status",('Active','Inactive'))
		if status == 'Active':
			st.text("Status is Active")
		else:
			st.warning("Not Active Yet")

		# SelectBox
		occupation = st.selectbox("Your Occupation",['Data Scientist','Programmer','Doctor','Businessman'])
		st.write("You selected this option",occupation)

		# MultiSelect
		location = st.multiselect("Where do you stay",("London","New York","Accra","Kiev","Berlin","New Delhi"))
		st.write("You selected",len(location),"location")


		# Slider
		salary = st.slider("What is your salary",1000,10000)

		# Buttons
		st.button("Simple Button")


	if st.checkbox("Display Code For Widget [Checkbox,Radio Button,SelectBox,MultiSelect,Button,Slider]"):
		st.code(raw_code_widget)

	### Ends Here
	### Begin Here
	if st.checkbox("Preview For Inputs[Text Input,Date,Time"):
		# Text Input
		name = st.text_input("Enter Name","Type Here...")
		if st.button('Submit'):
		    result = name.title()
		    st.success(result)
		else:
		    st.write("Press the above button..")

		# Text Area
		c_text = st.text_area("Enter Text","Type Here...")
		if st.button('Analyze'):
		    c_result = c_text.title()
		    st.success(c_result)
		else:
		    st.write("Press the above button..")


		#  Date Input
		import datetime,time
		today = st.date_input("Today is",datetime.datetime.now())


		# Time Input
		t = st.time_input("The time now is",datetime.time())


	if st.checkbox("Display Code For Inputs[Text Input,Date,Time"):
		st.code(raw_code_inputs)
	### Ends Here
	### Begin Here

	if st.checkbox("Preview For [Sidebar,Spinner,Progressbar,Balloon,etc]"):
		# SIDE Bar
		st.sidebar.header("Side Bar Header")
		st.sidebar.text("Hello")


		# Display JSON
		st.text("Display JSON")
		st.json({'name':'hello','age':34})

		# Display Raw Code
		st.text("Display Raw Code")
		st.code("import numpy as np")


		st.text("Display Raw Code Alternative Method")
		with st.echo():
			# This will also be shown
			import pandas as pd 

			df = pd.DataFrame()


		# Progress Bar
		# import time
		# my_bar = st.progress(0)
		# for p  in range(10):
		# 	my_bar.progress(p +1)

		# Spinner
		with st.spinner("Waiting .."):
			time.sleep(5)
		st.success("Finished!")


		# Cache For Performance
		@st.cache
		def run_multiple():
			return range(100)
		# Display the result of function
		st.write(run_multiple())

	if st.checkbox("Display Code For [Sidebar,Spinner,Progressbar,Balloon,etc]"):
		st.code(raw_code_others)

	# Ends Here

	# SIDE Bar
	st.sidebar.header("Streamlit Quick Reference")
	st.sidebar.subheader("Streamlit Is Awesome")
	st.sidebar.text("This is a sidebar")
	st.sidebar.markdown("[Check the Docs For More](https://streamlit.io/docs/)")

	st.sidebar.header("About")
	st.sidebar.text("Jesus Saves@JCharisTech")
	st.sidebar.markdown("[JCharisTech](https://jcharistech.com)")


if __name__ == '__main__':
	main()

