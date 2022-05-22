int main()
{
    char *kernel_data_addr = (char*)0x921b000;
    char kernel_data = *kernel_data_addr;
    printf("I have reached here.\n");
    return 0;
}
