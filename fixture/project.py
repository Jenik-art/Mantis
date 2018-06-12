from model.project import Project
import time
class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add(self, project):
        wd = self.app.wd
        self.open_project_page()
        #wd.find_element_by_css_selector("input[type='submit']").click()
        wd.find_element_by_xpath("//table[3]/tbody/tr[1]/td/form/input[2]").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input.button").click()
        time.sleep(10)
        self.return_project_page(wd)
        project_cache = None

    def fill_project_form(self,project):
        wd = self.app.wd
        self.change_field_value("name", project.name)

    def change_field_value(self, field_name, text):
         wd = self.app.wd
         if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
            wd.find_element_by_name(field_name).click()

    def return_project_page(self,wd):
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def open_project_page(self):
        wd = self.app.wd
        #self.app.open_home_page()
        #self.app.session.login("administrator", "root")
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    project_cache = None

    def get_group_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                name = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("id")
                self.project_cache.append(Project(name=name, id=id))
        return list(self.project_cache)


    def click_edit_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//table[3]/tbody/tr/td[1]/a")[index].click()

    def delete(self,index):
        wd = self.app.wd
        self.open_project_page()
        self.click_edit_by_index(index)
        wd.find_element_by_xpath("//div[4]/form/input[3]").click()
        wd.find_element_by_xpath("//input[@class='button']").click()