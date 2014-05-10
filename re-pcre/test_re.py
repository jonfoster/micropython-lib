import re

m = re.search(r"a+", "caaab")
assert m.group(0) == "aaa"

m = re.match(r"(?ms)foo.*\Z", "foo\nbar")
assert m.group(0) == "foo\nbar"

assert re.match(r"a+", "caaab") is None
m = re.match(r"a+", "aaaab")
assert m.group(0) == "aaaa"

assert re.sub("a", "z", "caaab") == "czzzb"
assert re.sub("a+", "z", "caaab") == "czb"

assert re.sub("a", lambda m: m.group(0) * 2, "caaab") == "caaaaaab"

m = re.match(r"(\d+)\.(\d+)", "24.1632")
assert m.groups() == ('24', '1632')
assert m.group(2, 1) == ('1632', '24')

assert re.escape(r"1243*&[]_dsfAd") == r"1243\*\&\[\]_dsfAd"
