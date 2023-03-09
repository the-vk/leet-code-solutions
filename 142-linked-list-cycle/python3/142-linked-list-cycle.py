class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for e in emails:
            e = self.normalizeEmail(e)
            if e not in unique_emails:
                unique_emails.add(e)
        return len(unique_emails)
            
    def normalizeEmail(self, email: str) -> str:
        local, domain = email.split('@')
        primary, *rest = local.split('+')
        primary = primary.replace('.', '')
        return primary + '@' + domain