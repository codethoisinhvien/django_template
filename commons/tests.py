from django.test import TestCase
from commons.authorization.adapter import Adapter
from commons.authorization.author import IsAuthor
# Create your tests here.
import casbin
en = casbin.Enforcer('commons/authorization/model.conf',Adapter())
en.load_policy()
# en.add_policy('eve1', 'data3', 'read')
# en.add_policy('eve2', 'data3', 'read')
# en.add_policy('eve1', 'data3', 'read')
en.delete_permissions_for_user('eve2')
# en.delete_permissions_for_user('eve2')
print(en.get_all_subjects())
# en.delete_permission('eve2')

