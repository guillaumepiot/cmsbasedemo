from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from admin_tools.dashboard import Dashboard, AppIndexDashboard
from admin_tools.dashboard import modules


# to activate your index dashboard add the following to your settings.py:
#
# ADMIN_TOOLS_INDEX_DASHBOARD = 'test_proj.dashboard.CustomIndexDashboard'


# class StatsDashboardModule(modules.ModelList):
#     title = 'Stats'
#     template = 'admin_tools/dashboard/modules/stats.html'
#     position = 'left'
#     show_title = False

#     def init_with_context(self, context):
#         request = context['request']
#         data = []
#         self.children.append(['Dataset', data])

class CustomIndexDashboard(Dashboard):

    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)

        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            _('Quick links'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_('<i class="icon-plus"></i> Return to site'), '/', 'action'],
                [_('<i class="icon-edit"></i> Change password'), reverse('admin:password_change'), 'action'],
                #[_('Log out'), reverse('admin:logout'), 'action'],
            ],
            position = 'right'
        ))

        # append an app list module for "Applications"
        # self.children.append(modules.AppList(
        #     _('Applications'),
        #     exclude=['django.contrib.*'],
        # ))

        # append an app list module for "Administration"
        # self.children.append(modules.AppList(
        #     _('Administration'),
        #     models=('django.contrib.*',),
        # ))

        # self.children.append(StatsDashboardModule(
        #     _('Statistics'),
        #     position = 'left'
        # ))

        
        

        # append a recent actions module
        self.children.append(
             modules.RecentActions(_('Recent Actions'), 10, position = 'right'),
            
        )

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        pass



# to activate your app index dashboard add the following to your settings.py:
#
# ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'test_proj.dashboard.CustomAppIndexDashboard'

class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for test_proj.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(include_list=self.get_app_content_types()),
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        pass