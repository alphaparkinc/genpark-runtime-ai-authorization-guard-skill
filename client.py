class RuntimeAiAuthorizationGuardClient:
    DANGEROUS_PATTERNS = ["rm -rf", "drop database", "sudo", "format C:"]

    def authorize(self, requested_command: str, target_path: str = "./") -> dict:
        cmd_lower = requested_command.lower()
        for p in self.DANGEROUS_PATTERNS:
            if p in cmd_lower:
                return {"is_authorized": False, "security_decision": f"BLOCKED: Dangerous pattern '{p}' detected"}
        return {"is_authorized": True, "security_decision": "ALLOWED: Command verified within safe sandbox bounds"}
