def litresUsed(l, m_t):
    lpm = (l * 100) / m_t
    return lpm

print(litresUsed(int(input('Enter how many litres:  ')), int(input('Enter how many miles traveled:  '))))