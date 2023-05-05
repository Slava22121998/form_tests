from main import Browser

br = Browser()

def test_bring_out_part():
    value = 123456
    current_balance = br.current_balance
    assert br.bring_out_part(value=value) == current_balance - value, "balance has not been updated"

def test_bring_out_all():
    assert br.bring_out_all() == 0, "balance has not been updated" 