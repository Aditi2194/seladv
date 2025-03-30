import time
import pytest
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Utilities.test_data import TestData
 
@pytest.mark.usefixtures("driver_initialization")
class TestScenario1():
    def test_scenario_1(self):
        basePage = BasePage(self.driver)
        homePage = HomePage(self.driver)
 
        #explicit wait time untill all the elements in the DOM are available.
        homePage.verifyAllElementsLoaded(self.driver)
 
        #using the scrollIntoView() method to scroll to the WebElement ‘Explore all Integrations’
        #using the seamlessCollaborationText to scroll as using exploreAllIntegrationsLink goes out of view
        homePage.scrollElementIntoView(TestData.seamlessCollaborationText)
 
        #click on ‘Explore all Integrations’ link to open a page in new tab
        time.sleep(5)
        homePage.openLinkInNewTab(TestData.exploreAllIntegrationsLink)
 
        #save the window handles in a List (or array). Print the window handles
        #of the opened windows
        windowHandles = self.driver.window_handles
        for index, handle in enumerate(windowHandles):
            print("Window Handle {0}: {1}".format(index, handle))
        time.sleep(10)
        assert len(windowHandles) == 2, ('Count of Window Handles is not as expected! '
                                         'Expected : 2, Actual: {0}').format(len(windowHandles))
       
        #switch to a new tab and verify the URL of the new tab
        self.driver.switch_to.window(windowHandles[-1])
        time.sleep(5)
        assert self.driver.current_url == TestData.integrationsTabUrl, (
            'URL of the new Tab does not match with the expected!'
            'Expected: {0} Actual: {1}'.format(TestData.integrationsTabUrl, self.driver.current_url))
       
        #on that page, scroll to the page where the WebElement
        #(Codeless Automation) is present.
        homePage.scrollElementIntoView(TestData.codelessAutomationLink)
        time.sleep(2)
 
        #click ‘INTEGRATE TESTING WHIZ WITH LAMBDATEST’ link for Testing Whiz.
        basePage.click_on_element(TestData.codelessAutomationLink)
        time.sleep(2)
        basePage.click_on_element(TestData.testingWhizLink)
        time.sleep(2)
 
        #check if the title of the page is ‘TestingWhiz Integration With LambdaTest’.
        #print(self.driver.title) this returns the title of the page as
        #"Running Automation Tests Using TestingWhiz LambdaTest | LambdaTest"
        #Using different method to Check if the title of the page is ‘TestingWhiz Integration With LambdaTest’ .
        assert basePage.get_text_in_element(
            TestData.testingWhizPageTitle) == "TestingWhiz Integration With LambdaTest", (
            'Title of the Page does not match!'
            'Expected Title: {0} Actual Title: {1}'.format("TestingWhiz Integration With LambdaTest",
                                                           self.driver.title))
       
        #closing the current window and switch to first window.
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
 
        #print the current window count.
        print("Current Count of Window Handles: ", len(self.driver.window_handles))
 
        #on the current window, set the URL to https://www.lambdatest.com/blog.
        self.driver.get(TestData.blogUrl)
 
        #click on the ‘Community’ link and verify the URL
        basePage.click_on_element(TestData.communityLink)
        assert self.driver.current_url == TestData.communityPageUrl, ('URL of the Community Page does not match with '
                                                                      'the expected!'
                                                                      'Expected: {0} Actual: {1}'.format(
            TestData.communityPageUrl, self.driver.current_url))