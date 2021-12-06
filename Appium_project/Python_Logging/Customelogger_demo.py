import logging
import Python_Logging.Customlogger as cl

class CustomLoggerDemo():
    log = cl.custom_logger()

    def methodOne(self):
        self.log.critical("This is a critical")
        self.log.error("This is a error msg")
        self.log.warning("Warn msg")
        self.log.info("Info msg")
        self.log.debug("Debug msg")

    def methodTwoo(self):
        m2 = cl.custom_logger()
        m2.critical("Critical Msg")
        m2.error("Error msg")
        m2.warning("Warn msg")
        m2.info("Info msg")
        m2.debug("Debug msg")

    def methodTwo(self):
        self.log.critical("This is a critical...")
        self.log.error("This is a error msg...")
        self.log.warning("Warn msg...")
        self.log.info("Info msg...")
        self.log.debug("Debug msg...")

cld =CustomLoggerDemo()
cld.methodOne()
cld.methodTwo()
cld.methodTwoo()