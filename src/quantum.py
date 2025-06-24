class EntanglementValidator:
    def verify_triplicate(self, decision):
        qbits = [Qubit(decision) for _ in range(3)]
        return all(q.collapse() == qbits[0].collapse() for q in qbits)
