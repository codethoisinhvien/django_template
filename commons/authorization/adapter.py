from casbin import persist

from django.db.models import Q

from commons.models import CasbinRule


class Adapter(persist.Adapter):
    """the interface for Casbin adapters."""

    def load_policy(self, model):
        """loads all policy rules from the storage."""
        lines = CasbinRule.objects.all()

        for line in lines:
            persist.load_policy_line(str(line), model)

    def _save_policy_line(self, ptype, rule):
        line = CasbinRule(ptype=ptype)
        for i, v in enumerate(rule):
            setattr(line, 'v{}'.format(i), v)
        line.save()

    def save_policy(self, model):
        """saves all policy rules to the storage."""
        for sec in ["p", "g"]:
            if sec not in model.model.keys():
                continue
            for ptype, ast in model.model[sec].items():
                for rule in ast.policy:
                    self._save_policy_line(ptype, rule)
        return True

    def add_policy(self, sec, ptype, rule):
        """adds a policy rule to the storage."""
        self._save_policy_line(ptype, rule)

    def remove_policy(self, sec, ptype, rule):
        """removes a policy rule from the storage."""
        print("21312323")
        if sec in ["p", "g"]:
            condition = Q(ptype=ptype)
            data = dict(zip(['v0', 'v1', 'v2', 'v3', 'v4', 'v5'], rule))
            for item in data:
                condition &= Q(**{item: data[item]})

            print(condition)
            check = CasbinRule.objects.filter(condition)
            if check.exists():
                check.delete()
                return True
            else:
                return False
        else:
            return False

        return False

    def remove_filtered_policy(self, sec, ptype, field_index, *field_values):
        condition = Q(ptype=ptype)

        query = CasbinRule.objects.filter(ptype=ptype)
        if not (0 <= field_index <= 5):
            return False
        if not (1 <= field_index + len(field_values) <= 6):
            return False
        data = dict(zip(['v0', 'v1', 'v2', 'v3', 'v4', 'v5'], field_values))
        for item in data:
            condition &= Q(**{item: data[item]})
        query = query.filter(condition)

        r = query.delete()

        return True if r is not None else False
