from rest_framework import permissions



class CustomUpdatePermission(permissions.BasePermission):
    """
    Permission class to check that a user can update his own resource only
    """

    def has_permission(self, request, view):
        # check that its an update request and user is modifying his resource only
        # print (view.action)
        print(view.kwargs)
        print(request.user.id)
        if view.action == 'update' or view.action == 'partial_update' and int(view.kwargs['pk'])!=request.user.id:
            # print('Vasya Loh')
            # print(view.kwargs['pk']!=request.user.id)
            return False # not grant access
        return True # grant access otherwise










# class DjangoModelPermissionsWithRead(permissions.DjangoModelPermissions):
#
#     perms_map = {
#         'GET': ['%(app_label)s.view_%(model_name)s'],
#         'OPTIONS': [],
#         'HEAD': [],
#         'POST': ['%(app_label)s.add_%(model_name)s'],
#         'PUT': ['%(app_label)s.change_%(model_name)s'],
#         'PATCH': ['%(app_label)s.change_%(model_name)s'],
#         'DELETE': ['%(app_label)s.delete_%(model_name)s'],
#     }

    # def has_permission(self, request, view):
    #
    #     if request.user.username == 'ulan':
    #         return True
    #
    #     return False


