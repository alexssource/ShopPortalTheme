# Identify the parent ID and assign it to the newrep variable.
newrep = AdminConfig.getid('/ResourceEnvironmentProvider:WP DynamicContentSpotMappings/')
print newrep

# Identify the required attributes
print AdminConfig.required('J2EEResourceProperty')

# Identify all possible attributes
print AdminConfig.attributes('J2EEResourceProperty')

# Set up the required attributes and assign it to the variables:
name01 = ['name','ShopPortalTheme_asa']
val01 = ['value', 'res:/wps/themeModules/modules/asa/jsp/asa.jsp, wp_analytics']

name02 = ['name','ShopPortalTheme_asaHead']
val02 = ['value', 'res:/wps/themeModules/modules/asa/jsp/head.jsp, wp_analytics']

name03 = ['name','ShopPortalTheme_asaPortlet']
val03 = ['value', 'res:/wps/themeModules/modules/asa/jsp/asaPortlet.jsp, wp_analytics']

name04 = ['name','ShopPortalTheme_commonActions']
val04 = ['value', 'res:/ShopPortalThemeDynamic/themes/html/dynamicSpots/commonActions.jsp']

name05 = ['name','ShopPortalTheme_crumbTrail']
val05 = ['value', 'res:/ShopPortalThemeDynamic/themes/html/dynamicSpots/crumbTrail.jsp?rootClass=wpthemeCrumbTrail&startLevel=2']

name06 = ['name','ShopPortalTheme_footer']
val06 = ['value', 'res:/ShopPortalThemeDynamic/themes/html/dynamicSpots/footer.jsp']

name07 = ['name','ShopPortalTheme_head']
val07 = ['value', 'res:/ShopPortalThemeDynamic/themes/html/dynamicSpots/head.jsp']

name08 = ['name','ShopPortalTheme_layout']
val08 = ['value', 'lm:template']

name09 = ['name','ShopPortalTheme_mobileNav']
val09 = ['value', 'mvc:smartphone/tablet@res:/ShopPortalThemeDynamic/themes/html/dynamicSpots/mobileNavigation.jsp']

name10 = ['name','ShopPortalTheme_mobileSearch']
val10 = ['value', 'mvc:smartphone/tablet@res:/ShopPortalThemeDynamic/themes/html/dynamicSpots/search.jsp']

name11 = ['name','ShopPortalTheme_pageModeToggle']
val11 = ['value', 'res:/ShopPortalThemeDynamic/themes/html/dynamicSpots/pageModeToggle.jsp,wp_toolbar']

name12 = ['name','ShopPortalTheme_preview']
val12 = ['value', 'res:/wps/themeModules/modules/pagebuilder/jsp/preview.jsp,wp_preview']

name13 = ['name','ShopPortalTheme_primaryNav']
val13 = ['value', 'mvc:res:/ShopPortalThemeDynamic/themes/html/dynamicSpots/navigation.jsp?rootClass=wpthemePrimaryNav%2520wpthemeLeft&startLevel=1']

name14 = ['name','ShopPortalTheme_projectMenu']
val14 = ['value', 'res:/wps/themeModules/modules/pagebuilder/jsp/projectMenu.jsp,wp_project_menu']

name15 = ['name','ShopPortalTheme_search']
val15 = ['value', 'mvc:res:/ShopPortalThemeDynamic/themes/html/dynamicSpots/search.jsp,smartphone@,tablet@']

name16 = ['name','ShopPortalTheme_secondaryNav']
val16 = ['value', 'mvc:res:/ShopPortalThemeDynamic/themes/html/dynamicSpots/navigation.jsp?rootClass=wpthemeSecondaryNav&startLevel=2&levelsDisplayed=2']

name17 = ['name','ShopPortalTheme_sideNav']
val17 = ['value', 'mvc:res:/ShopPortalThemeDynamic/themes/html/dynamicSpots/sideNavigation.jsp?startLevel=2']

name18 = ['name','ShopPortalTheme_status']
val18 = ['value', 'res:/ShopPortalThemeDynamic/themes/html/dynamicSpots/status.jsp, wp_status_bar']

name19 = ['name','ShopPortalTheme_toolbar']
val19 = ['value', 'res:/wps/themeModules/modules/pagebuilder/jsp/toolbar.jsp,wp_toolbar']

name20 = ['name','ShopPortalTheme_topNav']
val20 = ['value', 'res:/ShopPortalThemeDynamic/themes/html/dynamicSpots/navigation.jsp?rootClass=wpthemeHeaderNav&startLevel=0&primeRoot=true']

rpAttrs01 = [ name01, val01 ]
rpAttrs02 = [ name02, val02 ]
rpAttrs03 = [ name03, val03 ]
rpAttrs04 = [ name04, val04 ]
rpAttrs05 = [ name05, val05 ]
rpAttrs06 = [ name06, val06 ]
rpAttrs07 = [ name07, val07 ]
rpAttrs08 = [ name08, val08 ]
rpAttrs09 = [ name09, val09 ]
rpAttrs10 = [ name10, val10 ]
rpAttrs11 = [ name11, val11 ]
rpAttrs12 = [ name12, val12 ]
rpAttrs13 = [ name13, val13 ]
rpAttrs14 = [ name14, val14 ]
rpAttrs15 = [ name15, val15 ]
rpAttrs16 = [ name16, val16 ]
rpAttrs17 = [ name17, val17 ]
rpAttrs18 = [ name18, val18 ]
rpAttrs19 = [ name19, val19 ]
rpAttrs20 = [ name20, val20 ]

# Get the J2EE resource property set:
propSet = AdminConfig.showAttribute(newrep, 'propertySet')
print propSet

# Create a J2EE resource property:
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs01)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs02)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs03)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs04)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs05)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs06)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs07)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs08)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs09)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs10)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs11)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs12)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs13)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs14)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs15)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs16)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs17)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs18)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs19)
print AdminConfig.create('J2EEResourceProperty', propSet, rpAttrs20)

# Save the configuration changes:
AdminConfig.save()