from turtle import position
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='AWS SSO V-Groups', width=600, height=300)

# Window to Authenticate the credentials
with dpg.window(label="Authenticate Credentials", width=300):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

with dpg.window(label="Sync Users from AD Groups", width=500):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)
    


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()