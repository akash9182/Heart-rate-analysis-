package nodomain.freeyourgadget.gadgetbridge.service.btle.actions;

import android.bluetooth.BluetoothGatt;
import android.content.Context;
import android.widget.Toast;

import nodomain.freeyourgadget.gadgetbridge.impl.GBDevice;
import nodomain.freeyourgadget.gadgetbridge.util.GB;

public class SetDeviceStateAction extends PlainAction {
    private final GBDevice device;
    private final GBDevice.State deviceState;
    private final Context context;

    public SetDeviceStateAction(GBDevice device, GBDevice.State deviceState, Context context) {
        this.device = device;
        this.deviceState = deviceState;
        this.context = context;
    }

    @Override
    public boolean run(BluetoothGatt gatt) {
        device.setState(deviceState);
        device.sendDeviceUpdateIntent(getContext());
        return true;
    }

    public Context getContext() {
        return context;
    }

    @Override
    public String toString() {
        return super.toString() + " to " + deviceState;
    }
//    GB.toast(getContext(), "Connected", Toast.LENGTH_SHORT, GB.INFO);

}
