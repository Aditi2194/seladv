from selenium.webdriver.common.by import By
 
 
class TestData:
    """
    This class stores all the test data and locators required for the test scenario automation
    """
   
    #URLs
    baseUrl = "https://www.lambdatest.com/"
    integrationsTabUrl = "https://www.lambdatest.com/integrations"
    blogUrl = "https://www.lambdatest.com/blog/"
    communityPageUrl = "https://community.lambdatest.com/"
 
    #Page Elements
    exploreAllIntegrationsLink = (By.LINK_TEXT, 'Explore all Integrations')
    seamlessCollaborationText = (By.XPATH, '//*[contains(text(),"Seamless Collaboration via Integration")]')
    #codelessAutomationLink = (By.XPATH, '//a[text()="Codeless Automation"]')
    codelessAutomationLink = (By.CSS_SELECTOR, '#__next .integration .left_bar li:nth-child(5) > a')
    testingWhizLink = (By.XPATH, '//a[text()="Integrate Testing Whiz with LambdaTest"]')
    testingWhizPageTitle = (By.XPATH, '//h1')
    communityLink = (By.XPATH, '//div[@class="menu-menu-1-container"]//a[text()="Community"]')
 
    #__next > div > section.pb-0.integration > div > div > div.w-full.sm\:w-3\/12.pr-30.left_bar > div > ul > li:nth-child(5) > a