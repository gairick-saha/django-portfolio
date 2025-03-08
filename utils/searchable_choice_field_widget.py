from django.forms import Widget, Media
from django.utils.safestring import mark_safe

class SearchableChoiceFieldWidget(Widget):
    template_name = 'custom-dropdown.html'
    
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.choices = []
        
    def render(self, name, value, attrs=None, renderer=None):
        if attrs is None:
            attrs = {}
            
        # Create hidden input for the actual value
        hidden_input = f'<input type="hidden" name="{name}" value="{value or ""}" id="id_{name}">'
        
        # Find the selected option label if any
        selected_label = "Select an option"
        selected_icon_html = ""
        for option_value, option_label in self.choices:
            if str(option_value) == str(value):
                selected_label = option_label
                if option_value and "devicon-" not in option_value:
                    selected_icon_html = f'<i class="devicon-{option_value} colored"></i>'
                elif option_value:
                    selected_icon_html = f'<i class="{option_value} colored"></i>'
                break
        
        # Create the initial button content
        button_content = ""
        if selected_icon_html:
            button_content = f'''
            <div class="content-container" style="display: flex; align-items: center; gap: 12px;">
                {selected_icon_html}
                <span style="font-size: 14px;">{selected_label}</span>
            </div>
            '''
        else:
            button_content = f'<span>{selected_label}</span>'
        
        # Create the searchable dropdown container
        dropdown_html = f'''
        <div class="searchable-dropdown" data-field-name="{name}">
            <div class="select-btn" style="display: flex; justify-content: space-between; align-items: center;">
                {button_content}
                <i class="fa fa-caret-down" style="margin-left: auto;"></i>
            </div>
            <div class="searchable-dropdown-content" style="display: none;">
                <div class="search">
                    <input type="text" placeholder="Search...">
                </div>
                <ul class="dropdown-options">
        '''
        
        # Add options from choices
        for option_value, option_label in self.choices:
            icon_html = ""
            if option_value:
                if "devicon-" not in option_value and option_value != "":
                    icon_html = f'<i class="devicon-{option_value}" style="font-size: 50px; display: flex; align-items: center; justify-content: center;"></i>'
                elif option_value != "":
                    icon_html = f'<i class="{option_value}" style="font-size: 50px; display: flex; align-items: center; justify-content: center;"></i>'
            
            selected_class = 'selected' if str(value) == str(option_value) else ''
            
            icon_display = icon_html if name == "logo" else ''
            margin_left = "margin-left: 10px;" if name == "logo" else ''
            dropdown_html += f'''
            <li value="{option_value}" class="{selected_class}" style="display: flex; align-items: center; padding: 8px 12px; cursor: pointer;">
                {icon_display}
                <p style="{margin_left}">{option_label}</p>
            </li>
            '''
        
        dropdown_html += '''
                </ul>
            </div>
        </div>
        '''
        
        return mark_safe(hidden_input + dropdown_html)
    
    def value_from_datadict(self, data, files, name):
        # This is crucial for Django to get the value from form submission
        return data.get(name)
    
    @property
    def media(self):
        return Media(
            css={
                'all': [
                    'https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css',
                    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css',
                    'admin/css/custom-dropdown.css'
                ]
            },
            js=[
                'https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js',
                'admin/js/custom-dropdown.js'
            ]
        )