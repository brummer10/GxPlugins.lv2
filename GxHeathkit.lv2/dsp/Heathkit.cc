// generated from file './/Heathkit.dsp' by dsp2cc:
// Code generated with Faust 0.9.90 (http://faust.grame.fr)


namespace Heathkit {

class Dsp: public PluginLV2 {
private:
	uint32_t fSamplingFreq;
	FAUSTFLOAT 	fslider0;
	FAUSTFLOAT	*fslider0_;
	double 	fRec0[2];
	double 	fConst0;
	double 	fConst1;
	double 	fConst2;
	double 	fConst3;
	double 	fConst4;
	double 	fConst5;
	double 	fConst6;
	double 	fConst7;
	double 	fConst8;
	double 	fConst9;
	double 	fConst10;
	double 	fConst11;
	double 	fConst12;
	FAUSTFLOAT 	fslider1;
	FAUSTFLOAT	*fslider1_;
	double 	fRec1[2];
	double 	fConst13;
	double 	fConst14;
	double 	fConst15;
	double 	fConst16;
	double 	fConst17;
	double 	fConst18;
	double 	fConst19;
	double 	fConst20;
	double 	fConst21;
	double 	fConst22;
	double 	fConst23;
	double 	fConst24;
	double 	fConst25;
	double 	fConst26;
	double 	fConst27;
	double 	fConst28;
	double 	fConst29;
	double 	fConst30;
	double 	fRec2[5];
	double 	fConst31;
	double 	fConst32;
	double 	fConst33;
	double 	fConst34;
	double 	fConst35;
	double 	fConst36;
	double 	fConst37;
	double 	fConst38;
	double 	fConst39;
	double 	fConst40;
	double 	fConst41;
	double 	fConst42;
	double 	fConst43;
	double 	fConst44;
	double 	fConst45;
	double 	fConst46;
	double 	fConst47;
	double 	fConst48;
	double 	fConst49;
	double 	fConst50;

	void connect(uint32_t port,void* data);
	void clear_state_f();
	void init(uint32_t samplingFreq);
	void compute(int count, FAUSTFLOAT *input0, FAUSTFLOAT *output0);

	static void clear_state_f_static(PluginLV2*);
	static void init_static(uint32_t samplingFreq, PluginLV2*);
	static void compute_static(int count, FAUSTFLOAT *input0, FAUSTFLOAT *output0, PluginLV2*);
	static void del_instance(PluginLV2 *p);
	static void connect_static(uint32_t port,void* data, PluginLV2 *p);
public:
	Dsp();
	~Dsp();
};



Dsp::Dsp()
	: PluginLV2() {
	version = PLUGINLV2_VERSION;
	id = "Heathkit";
	name = N_("Heathkit");
	mono_audio = compute_static;
	stereo_audio = 0;
	set_samplerate = init_static;
	activate_plugin = 0;
	connect_ports = connect_static;
	clear_state = clear_state_f_static;
	delete_instance = del_instance;
}

Dsp::~Dsp() {
}

inline void Dsp::clear_state_f()
{
	for (int i=0; i<2; i++) fRec0[i] = 0;
	for (int i=0; i<2; i++) fRec1[i] = 0;
	for (int i=0; i<5; i++) fRec2[i] = 0;
}

void Dsp::clear_state_f_static(PluginLV2 *p)
{
	static_cast<Dsp*>(p)->clear_state_f();
}

inline void Dsp::init(uint32_t samplingFreq)
{
	fSamplingFreq = samplingFreq;
	fConst0 = double(min(1.92e+05, max(1.0, (double)fSamplingFreq)));
	fConst1 = (1.5990596744582e-19 * fConst0);
	fConst2 = ((fConst0 * ((fConst0 * (0 - (5.91755671934861e-16 + fConst1))) - 8.77667425136098e-14)) - 2.40648433568958e-13);
	fConst3 = (1.49352173594396e-19 * fConst0);
	fConst4 = (2.24765636953407e-13 + (fConst0 * (8.19741375077115e-14 + (fConst0 * (5.5269979758716e-16 + fConst3)))));
	fConst5 = (1.39738093023942e-19 * fConst0);
	fConst6 = (9.6026564512814e-12 + (fConst0 * (1.5282984964354e-13 + (fConst0 * (5.3724044276275e-16 + fConst5)))));
	fConst7 = (3.338189221485e-19 * fConst0);
	fConst8 = (1.68281447068286e-14 + (fConst0 * (fConst7 - 6.81291052439413e-15)));
	fConst9 = (1.99821185793116e-18 * fConst0);
	fConst10 = ((fConst0 * (6.67357931217107e-15 + fConst9)) - 1.64981810851261e-14);
	fConst11 = (1.31881982623457e-19 * fConst0);
	fConst12 = ((fConst0 * (4.40456234603291e-16 + fConst11)) - 1.08887995161832e-15);
	fConst13 = (2.2032048861801e-20 * fConst0);
	fConst14 = (1.11065755065069e-15 + (fConst0 * (fConst13 - 4.49652094610013e-16)));
	fConst15 = (2.40648433568958e-13 + (fConst0 * ((fConst0 * (5.91755671934861e-16 - fConst1)) - 8.77667425136098e-14)));
	fConst16 = ((fConst0 * (8.19741375077115e-14 + (fConst0 * (fConst3 - 5.5269979758716e-16)))) - 2.24765636953407e-13);
	fConst17 = ((fConst0 * (1.5282984964354e-13 + (fConst0 * (fConst5 - 5.3724044276275e-16)))) - 9.6026564512814e-12);
	fConst18 = (6.3962386978328e-19 * fConst0);
	fConst19 = faustpower<2>(fConst0);
	fConst20 = (4.81296867137917e-13 + (fConst19 * (fConst18 - 1.18351134386972e-15)));
	fConst21 = (5.97408694377584e-19 * fConst0);
	fConst22 = ((fConst19 * (1.10539959517432e-15 - fConst21)) - 4.49531273906814e-13);
	fConst23 = (5.58952372095769e-19 * fConst0);
	fConst24 = ((fConst19 * (1.0744808855255e-15 - fConst23)) - 1.92053129025628e-11);
	fConst25 = ((fConst19 * (1.18351134386972e-15 + fConst18)) - 4.81296867137917e-13);
	fConst26 = (4.49531273906814e-13 + (fConst19 * (0 - (1.10539959517432e-15 + fConst21))));
	fConst27 = (1.92053129025628e-11 + (fConst19 * (0 - (1.0744808855255e-15 + fConst23))));
	fConst28 = (1.7553348502722e-13 - (9.5943580467492e-19 * fConst19));
	fConst29 = ((8.96113041566376e-19 * fConst19) - 1.63948275015423e-13);
	fConst30 = ((8.38428558143654e-19 * fConst19) - 3.05659699287079e-13);
	fConst31 = (5.27527930493826e-19 * fConst0);
	fConst32 = (8.80912469206581e-16 + fConst31);
	fConst33 = (7.99284743172464e-18 * fConst0);
	fConst34 = (0 - (1.33471586243421e-14 + fConst33));
	fConst35 = (1.335275688594e-18 * fConst0);
	fConst36 = (1.36258210487883e-14 - fConst35);
	fConst37 = (8.81281954472039e-20 * fConst0);
	fConst38 = (8.99304189220025e-16 - fConst37);
	fConst39 = (8.99304189220025e-16 + fConst37);
	fConst40 = (0 - (1.36258210487883e-14 + fConst35));
	fConst41 = (1.33471586243421e-14 - fConst33);
	fConst42 = (8.80912469206581e-16 - fConst31);
	fConst43 = (1.68281447068286e-14 + (fConst0 * (6.81291052439413e-15 + fConst7)));
	fConst44 = ((fConst0 * (fConst9 - 6.67357931217107e-15)) - 1.64981810851261e-14);
	fConst45 = ((fConst0 * (fConst11 - 4.40456234603291e-16)) - 1.08887995161832e-15);
	fConst46 = (1.11065755065069e-15 + (fConst0 * (4.49652094610013e-16 + fConst13)));
	fConst47 = ((2.002913532891e-18 * fConst19) - 3.36562894136573e-14);
	fConst48 = (3.29963621702522e-14 + (1.1989271147587e-17 * fConst19));
	fConst49 = (2.17775990323665e-15 + (7.91291895740739e-19 * fConst19));
	fConst50 = ((1.32192293170806e-19 * fConst19) - 2.22131510130138e-15);
	clear_state_f();
}

void Dsp::init_static(uint32_t samplingFreq, PluginLV2 *p)
{
	static_cast<Dsp*>(p)->init(samplingFreq);
}

void always_inline Dsp::compute(int count, FAUSTFLOAT *input0, FAUSTFLOAT *output0)
{
#define fslider0 (*fslider0_)
#define fslider1 (*fslider1_)
	double 	fSlow0 = (0.007000000000000006 * double(fslider0));
	double 	fSlow1 = (0.007000000000000006 * double(fslider1));
	for (int i=0; i<count; i++) {
		fRec0[0] = (fSlow0 + (0.993 * fRec0[1]));
		double fTemp0 = (2.5653123018451e-11 + (fConst0 * (fConst6 + (fRec0[0] * (fConst4 + (fConst2 * fRec0[0]))))));
		fRec1[0] = (fSlow1 + (0.993 * fRec1[1]));
		fRec2[0] = ((double)input0[i] - (((((fRec2[2] * (1.53918738110706e-10 + (fConst19 * (fConst30 + (fRec0[0] * (fConst29 + (fConst28 * fRec0[0]))))))) + (fRec2[1] * (1.02612492073804e-10 + (fConst0 * (fConst27 + (fRec0[0] * (fConst26 + (fConst25 * fRec0[0])))))))) + (fRec2[3] * (1.02612492073804e-10 + (fConst0 * (fConst24 + (fRec0[0] * (fConst22 + (fConst20 * fRec0[0])))))))) + (fRec2[4] * (2.5653123018451e-11 + (fConst0 * (fConst17 + (fRec0[0] * (fConst16 + (fConst15 * fRec0[0])))))))) / fTemp0));
		double fTemp1 = max(-1.12, min(1.2, (fConst19 * (((((fRec2[2] * (fConst50 + ((fRec1[0] * (fConst49 + (fConst48 * fRec0[0]))) + (fConst47 * fRec0[0])))) + (fRec2[0] * (fConst46 + ((fRec1[0] * (fConst45 + (fConst44 * fRec0[0]))) + (fConst43 * fRec0[0]))))) + (fConst0 * ((fRec2[1] * (((fRec1[0] * (fConst42 + (fConst41 * fRec0[0]))) + (fConst40 * fRec0[0])) - fConst39)) + (fRec2[3] * (fConst38 + ((fConst36 * fRec0[0]) + (fRec1[0] * ((fConst34 * fRec0[0]) - fConst32)))))))) + (fRec2[4] * (fConst14 + ((fRec1[0] * (fConst12 + (fConst10 * fRec0[0]))) + (fConst8 * fRec0[0]))))) / fTemp0))));
		double fTemp2 = (0 - fTemp1);
		double fTemp3 = exp((4 * fTemp1));
		output0[i] = (FAUSTFLOAT)(0.25 * ((fTemp3 - exp((4.8 * fTemp2))) / (fTemp3 + exp((4 * fTemp2)))));
		// post processing
		for (int i=4; i>0; i--) fRec2[i] = fRec2[i-1];
		fRec1[1] = fRec1[0];
		fRec0[1] = fRec0[0];
	}
#undef fslider0
#undef fslider1
}

void __rt_func Dsp::compute_static(int count, FAUSTFLOAT *input0, FAUSTFLOAT *output0, PluginLV2 *p)
{
	static_cast<Dsp*>(p)->compute(count, input0, output0);
}


void Dsp::connect(uint32_t port,void* data)
{
	switch ((PortIndex)port)
	{
	case LEVEL: 
		fslider0_ = (float*)data; // , 0.5, 0.0, 1.0, 0.01 
		break;
	case TONE: 
		fslider1_ = (float*)data; // , 0.5, 0.0, 1.0, 0.01 
		break;
	default:
		break;
	}
}

void Dsp::connect_static(uint32_t port,void* data, PluginLV2 *p)
{
	static_cast<Dsp*>(p)->connect(port, data);
}


PluginLV2 *plugin() {
	return new Dsp();
}

void Dsp::del_instance(PluginLV2 *p)
{
	delete static_cast<Dsp*>(p);
}

/*
typedef enum
{
   LEVEL, 
   TONE, 
} PortIndex;
*/

} // end namespace Heathkit
